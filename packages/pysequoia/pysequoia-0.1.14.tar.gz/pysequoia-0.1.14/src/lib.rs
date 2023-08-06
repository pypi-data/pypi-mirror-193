use pyo3::prelude::*;

use anyhow::Context as AnyhowContext;

use std::io::Write;

use sequoia_openpgp as openpgp;

use openpgp::policy::{Policy, StandardPolicy};
use openpgp::serialize::stream::{Encryptor, LiteralWriter, Message};
use openpgp::serialize::{
    stream::{Armorer, Signer},
    SerializeInto,
};
use openpgp::types::KeyFlags;

mod decrypt;

#[pyclass]
pub struct Cert {
    cert: openpgp::cert::Cert,
    policy: Box<dyn Policy>,
}

impl From<openpgp::cert::Cert> for Cert {
    fn from(cert: openpgp::cert::Cert) -> Self {
        Self {
            cert,
            policy: Box::new(StandardPolicy::new()),
        }
    }
}

#[pymethods]
impl Cert {
    #[staticmethod]
    pub fn from_file(path: String) -> PyResult<Self> {
        use openpgp::parse::Parse;
        Ok(openpgp::cert::Cert::from_file(path)?.into())
    }

    #[staticmethod]
    pub fn from_bytes(bytes: &[u8]) -> PyResult<Self> {
        use openpgp::parse::Parse;
        Ok(openpgp::cert::Cert::from_bytes(bytes)?.into())
    }

    #[staticmethod]
    pub fn generate(user_id: &str) -> PyResult<Self> {
        Ok(
            openpgp::cert::CertBuilder::general_purpose(None, Some(user_id))
                .generate()?
                .0
                .into(),
        )
    }

    pub fn merge(&self, new_cert: &Cert) -> PyResult<Cert> {
        Ok(merge_certs(self, new_cert)?)
    }

    pub fn __str__(&self) -> PyResult<String> {
        let armored = self.cert.armored();
        Ok(String::from_utf8(armored.to_vec()?)?)
    }

    pub fn __repr__(&self) -> String {
        format!("<Cert fingerprint={}>", self.cert.fingerprint())
    }

    #[getter]
    pub fn fingerprint(&self) -> PyResult<String> {
        Ok(format!("{:x}", self.cert.fingerprint()))
    }

    pub fn signer(&self, password: Option<String>) -> PyResult<PySigner> {
        if let Some(key) = self
            .cert
            .keys()
            .secret()
            .with_policy(&*self.policy, None)
            .alive()
            .revoked(false)
            .for_signing()
            .next()
        {
            let mut key = key.key().clone();
            if let Some(password) = password {
                key = key.decrypt_secret(&(password[..]).into())?;
            }
            let keypair = key.into_keypair()?;
            Ok(PySigner::new(Box::new(keypair)))
        } else {
            Err(anyhow::anyhow!("No suitable signing subkey for {}", self.cert).into())
        }
    }

    pub fn decryptor(&self, password: Option<String>) -> PyResult<decrypt::PyDecryptor> {
        if let Some(key) = self
            .cert
            .keys()
            .secret()
            .with_policy(&*self.policy, None)
            .alive()
            .revoked(false)
            .for_transport_encryption()
            .for_storage_encryption()
            .next()
        {
            let mut key = key.key().clone();
            if let Some(password) = password {
                key = key.decrypt_secret(&(password[..]).into())?;
            }
            let keypair = key.into_keypair()?;
            Ok(decrypt::PyDecryptor::new(Box::new(keypair)))
        } else {
            Err(anyhow::anyhow!("No suitable decryption subkey for {}", self.cert).into())
        }
    }
}

#[pyclass]
pub struct KeyServer {
    uri: String,
}

#[pymethods]
impl KeyServer {
    #[new]
    pub fn new(uri: &str) -> Self {
        Self { uri: uri.into() }
    }

    #[allow(clippy::should_implement_trait)]
    #[staticmethod]
    pub fn default() -> Self {
        Self {
            uri: "hkps://keys.openpgp.org".into(),
        }
    }

    pub fn get<'a>(&self, py: Python<'a>, fpr: String) -> PyResult<&'a PyAny> {
        let uri: String = self.uri.clone();
        pyo3_asyncio::tokio::future_into_py(py, async move {
            use openpgp::Fingerprint;
            let fpr: Fingerprint = fpr.parse()?;
            let mut ks = sequoia_net::KeyServer::new(sequoia_net::Policy::Encrypted, &uri)?;
            let cert = ks.get(fpr);
            let cert: Cert = cert.await?.into();
            Ok(cert)
        })
    }

    pub fn __repr__(&self) -> String {
        format!("<KeyServer uri={}>", self.uri)
    }
}

use std::sync::{Arc, Mutex};

#[pyclass]
#[derive(Clone)]
pub struct PySigner {
    inner: Arc<Mutex<Box<dyn openpgp::crypto::Signer + Send + Sync + 'static>>>,
    public: openpgp::packet::Key<
        openpgp::packet::key::PublicParts,
        openpgp::packet::key::UnspecifiedRole,
    >,
}

impl PySigner {
    pub fn new(inner: Box<dyn openpgp::crypto::Signer + Send + Sync + 'static>) -> Self {
        let public = inner.public().clone();
        Self {
            inner: Arc::new(Mutex::new(inner)),
            public,
        }
    }
}

impl openpgp::crypto::Signer for PySigner {
    fn public(
        &self,
    ) -> &openpgp::packet::Key<
        openpgp::packet::key::PublicParts,
        openpgp::packet::key::UnspecifiedRole,
    > {
        &self.public
    }

    fn sign(
        &mut self,
        hash_algo: openpgp::types::HashAlgorithm,
        digest: &[u8],
    ) -> openpgp::Result<openpgp::crypto::mpi::Signature> {
        self.inner.lock().unwrap().sign(hash_algo, digest)
    }
}

#[allow(clippy::upper_case_acronyms)]
#[pyclass]
struct WKD;

#[pymethods]
impl WKD {
    #[staticmethod]
    fn search(py: Python<'_>, email: String) -> PyResult<&PyAny> {
        pyo3_asyncio::tokio::future_into_py(py, async move {
            let certs = sequoia_net::wkd::get(email).await?;
            if let Some(cert) = certs.first() {
                let cert: Cert = cert.clone().into();
                Ok(Some(cert))
            } else {
                Ok(None)
            }
        })
    }
}

use openpgp_cert_d::CertD;
use std::path::PathBuf;

#[pyclass]
struct Store {
    cert_d: CertD,
    loc: PathBuf,
}

#[pymethods]
impl Store {
    #[new]
    pub fn new(loc: PathBuf) -> anyhow::Result<Self> {
        Ok(Self {
            cert_d: CertD::with_base_dir(&loc)?,
            loc,
        })
    }

    pub fn get(&self, id: String) -> anyhow::Result<Option<Cert>> {
        use openpgp::parse::Parse;
        if let Some((_tag, data)) = self.cert_d.get(&id)? {
            Ok(Some(openpgp::cert::Cert::from_bytes(&data)?.into()))
        } else {
            Ok(None)
        }
    }

    pub fn put(&mut self, cert: &Cert) -> anyhow::Result<Cert> {
        use openpgp::parse::Parse;
        use openpgp_cert_d::Data;
        let f = |new: Data, old: Option<Data>| {
            let merged = match old {
                Some(old) => {
                    let old = openpgp::cert::Cert::from_bytes(&old)?;
                    let new = openpgp::cert::Cert::from_bytes(&new)?;
                    old.merge_public(new)?.to_vec()?.into_boxed_slice()
                }
                None => new,
            };
            Ok(merged)
        };
        let (_tag, data) = self
            .cert_d
            .insert(cert.cert.to_vec()?.into_boxed_slice(), f)?;
        Ok(openpgp::cert::Cert::from_bytes(&data)?.into())
    }

    pub fn __repr__(&self) -> String {
        format!("<Store base={}>", self.loc.display())
    }
}

use openpgp_card_pcsc::PcscBackend;

#[pyclass]
struct Card {
    open: openpgp_card_sequoia::Card<openpgp_card_sequoia::state::Open>,
}

#[pymethods]
impl Card {
    #[staticmethod]
    pub fn open(ident: &str) -> anyhow::Result<Self> {
        Ok(Self {
            open: PcscBackend::open_by_ident(ident, None)?.into(),
        })
    }

    #[getter]
    pub fn cardholder(&mut self) -> anyhow::Result<Option<String>> {
        let mut transaction = self.open.transaction()?;
        Ok(transaction.cardholder_name()?)
    }

    #[getter]
    pub fn ident(&mut self) -> anyhow::Result<String> {
        let transaction = self.open.transaction()?;
        Ok(transaction.application_identifier()?.ident())
    }

    #[staticmethod]
    pub fn all() -> anyhow::Result<Vec<Card>> {
        Ok(PcscBackend::cards(None)?
            .into_iter()
            .map(|card| Self { open: card.into() })
            .collect())
    }

    pub fn signer(&mut self, pin: String) -> anyhow::Result<PySigner> {
        use sequoia_openpgp::crypto::Signer;

        struct CardSigner {
            public: openpgp::packet::Key<
                openpgp::packet::key::PublicParts,
                openpgp::packet::key::UnspecifiedRole,
            >,
            ident: String,
            pin: String,
        }

        impl openpgp::crypto::Signer for CardSigner {
            fn public(
                &self,
            ) -> &openpgp::packet::Key<
                openpgp::packet::key::PublicParts,
                openpgp::packet::key::UnspecifiedRole,
            > {
                &self.public
            }

            fn sign(
                &mut self,
                hash_algo: openpgp::types::HashAlgorithm,
                digest: &[u8],
            ) -> openpgp::Result<openpgp::crypto::mpi::Signature> {
                let backend = openpgp_card_pcsc::PcscBackend::open_by_ident(&self.ident, None)?;
                let mut card: openpgp_card_sequoia::Card<openpgp_card_sequoia::state::Open> =
                    backend.into();
                let mut transaction = card.transaction()?;

                transaction.verify_user_for_signing(self.pin.as_bytes())?;
                let mut user = transaction.signing_card().expect("This should not fail");

                let mut signer = user.signer(&|| {})?;
                signer.sign(hash_algo, digest)
            }
        }

        let public = {
            let mut transaction = self.open.transaction()?;

            transaction.verify_user_for_signing(pin.as_bytes())?;

            let mut user = transaction.signing_card().expect("This should not fail");

            let signer = user.signer(&|| {})?;
            signer.public().clone()
        };
        Ok(PySigner::new(Box::new(CardSigner {
            public,
            ident: self.ident()?,
            pin,
        })))
    }

    pub fn decryptor(&mut self, pin: String) -> anyhow::Result<decrypt::PyDecryptor> {
        use sequoia_openpgp::crypto::Decryptor;

        struct CardDecryptor {
            public: openpgp::packet::Key<
                openpgp::packet::key::PublicParts,
                openpgp::packet::key::UnspecifiedRole,
            >,
            ident: String,
            pin: String,
        }

        impl openpgp::crypto::Decryptor for CardDecryptor {
            fn public(
                &self,
            ) -> &openpgp::packet::Key<
                openpgp::packet::key::PublicParts,
                openpgp::packet::key::UnspecifiedRole,
            > {
                &self.public
            }
            fn decrypt(
                &mut self,
                ciphertext: &openpgp::crypto::mpi::Ciphertext,
                plaintext_len: Option<usize>,
            ) -> openpgp::Result<openpgp::crypto::SessionKey> {
                let backend = openpgp_card_pcsc::PcscBackend::open_by_ident(&self.ident, None)?;
                let mut card: openpgp_card_sequoia::Card<openpgp_card_sequoia::state::Open> =
                    backend.into();
                let mut transaction = card.transaction()?;

                transaction.verify_user(self.pin.as_bytes())?;
                let mut user = transaction.user_card().expect("user_card should not fail");

                let mut decryptor = user.decryptor(&|| {})?;
                decryptor.decrypt(ciphertext, plaintext_len)
            }
        }

        let public = {
            let mut transaction = self.open.transaction()?;

            transaction.verify_user_for_signing(pin.as_bytes())?;

            let mut user = transaction.user_card().expect("user_card should not fail");

            let decryptor = user.decryptor(&|| {})?;
            decryptor.public().clone()
        };
        Ok(decrypt::PyDecryptor::new(Box::new(CardDecryptor {
            public,
            ident: self.ident()?,
            pin,
        })))
    }

    pub fn __repr__(&mut self) -> anyhow::Result<String> {
        Ok(format!("<Card ident={}>", self.ident()?))
    }
}

#[pyfunction]
fn sign(signer: PySigner, data: String) -> PyResult<String> {
    use openpgp::serialize::stream::Signer;

    let mut sink = vec![];
    {
        let message = Message::new(&mut sink);

        let message = Armorer::new(message)
            .kind(openpgp::armor::Kind::Signature)
            .build()?;
        let message = Signer::new(message, signer).build()?;

        let mut message = LiteralWriter::new(message).build()?;

        message.write_all(data.as_bytes())?;

        message.finalize()?;
    }

    Ok(String::from_utf8_lossy(&sink).into())
}

#[pyfunction]
fn encrypt(signer: PySigner, recipients: Vec<PyRef<Cert>>, content: String) -> PyResult<String> {
    encrypt_for(signer, recipients, content).map_err(|e| e.into())
}

#[pyfunction]
fn minimize(cert: &Cert) -> PyResult<Cert> {
    Ok(minimize_cert(cert, &*cert.policy)?)
}

#[pymodule]
fn pysequoia(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Cert>()?;
    m.add_class::<KeyServer>()?;
    m.add_class::<WKD>()?;
    m.add_class::<Store>()?;
    m.add_class::<Card>()?;
    m.add_function(wrap_pyfunction!(sign, m)?)?;
    m.add_function(wrap_pyfunction!(encrypt, m)?)?;
    m.add_function(wrap_pyfunction!(minimize, m)?)?;
    m.add_function(wrap_pyfunction!(decrypt::decrypt, m)?)?;
    Ok(())
}

pub fn encrypt_for<U>(
    signer: PySigner,
    recipient_certs: Vec<PyRef<Cert>>,
    content: U,
) -> openpgp::Result<String>
where
    U: AsRef<[u8]> + Send + Sync,
{
    let mode = KeyFlags::empty()
        .set_storage_encryption()
        .set_transport_encryption();

    let mut recipients = vec![];
    for cert in recipient_certs.iter() {
        let mut found_one = false;
        for key in cert
            .cert
            .keys()
            .with_policy(&*cert.policy, None)
            .supported()
            .alive()
            .revoked(false)
            .key_flags(&mode)
        {
            recipients.push(key);
            found_one = true;
        }

        if !found_one {
            for key in cert
                .cert
                .keys()
                .with_policy(&*cert.policy, None)
                .supported()
                .revoked(false)
                .key_flags(&mode)
            {
                recipients.push(key);
                found_one = true;
            }
        }

        if !found_one {
            return Err(anyhow::anyhow!(
                "No suitable encryption subkey for {}",
                cert.cert
            ));
        }
    }

    let mut sink = vec![];

    let message = Message::new(&mut sink);

    let message = Armorer::new(message).build()?;

    let message = Encryptor::for_recipients(message, recipients)
        .build()
        .context("Failed to create encryptor")?;

    let message = Signer::new(message, signer).build()?;

    let mut message = LiteralWriter::new(message)
        .build()
        .context("Failed to create literal writer")?;

    message.write_all(content.as_ref())?;

    message.finalize()?;

    Ok(String::from_utf8(sink)?)
}

pub fn merge_certs(existing_cert: &Cert, new_cert: &Cert) -> openpgp::Result<Cert> {
    let merged_cert = existing_cert
        .cert
        .clone()
        .merge_public(new_cert.cert.clone())?;
    Ok(merged_cert.into())
}

pub fn minimize_cert(cert: &Cert, policy: &dyn Policy) -> openpgp::Result<Cert> {
    let cert = cert.cert.with_policy(policy, None)?;

    let mut acc = Vec::new();

    let c = cert.primary_key();
    acc.push(c.key().clone().into());

    for s in c.self_signatures() {
        acc.push(s.clone().into())
    }
    for s in c.self_revocations() {
        acc.push(s.clone().into())
    }

    for c in cert.userids() {
        acc.push(c.userid().clone().into());
        for s in c.self_signatures().take(1) {
            acc.push(s.clone().into())
        }
        for s in c.self_revocations() {
            acc.push(s.clone().into())
        }
    }

    let flags = KeyFlags::empty()
        .set_storage_encryption()
        .set_transport_encryption();

    let mut encryption_keys = cert
        .keys()
        .subkeys()
        .key_flags(&flags)
        .alive()
        .revoked(false)
        .collect::<Vec<_>>();

    if encryption_keys.is_empty() {
        encryption_keys = cert
            .keys()
            .subkeys()
            .key_flags(&flags)
            .revoked(false)
            .collect::<Vec<_>>();
    }

    for c in encryption_keys {
        acc.push(c.key().clone().into());
        for s in c.self_signatures().take(1) {
            acc.push(s.clone().into())
        }
        for s in c.self_revocations() {
            acc.push(s.clone().into())
        }
    }

    Ok(openpgp::cert::Cert::try_from(acc)?.into())
}

#[cfg(test)]
mod tests {
    use super::*;
    use openpgp::cert::prelude::*;
    use sequoia_openpgp as openpgp;
    use testresult::TestResult;

    #[test]
    fn test_armoring() -> TestResult {
        let cert = CertBuilder::general_purpose(None, Some("test@example.com"))
            .generate()?
            .0;
        assert!(cert.armored().to_vec().is_ok());
        Ok(())
    }
}
