from firebase_admin import firestore, credentials, initialize_app
import uuid
from decouple import config

database_config = {
    "type": config("type"),
    "project_id": config("project_id"),
    "private_key_id": config("private_key_id"),
    "private_key": config("private_key"),
    "client_email": config("client_email"),
    "client_id": config("client_id"),
    "auth_uri": config("auth_uri"),
    "token_uri": config("token_uri"),
    "auth_provider_x509_cert_url": config("auth_provider_x509_cert_url"),
    "client_x509_cert_url": config("client_x509_cert_url"),
    "universe_domain": config("universe_domain"),
}

# initialize firestoreDB
cred = credentials.Certificate(database_config)
default_app = initialize_app(cred)
db = firestore.client()
fololimo_ref = db.collection(config("FOLOLIMO_DB"))


def upload_to_firebase(data):
    try:
        id = uuid.uuid4().hex
        fololimo_ref.document(id).set(data)
        return True
    except Exception as e:
        print(f"Failed uploading to firebase: {str(e)} ..")
        return False
