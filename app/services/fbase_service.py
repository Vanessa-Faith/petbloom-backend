import firebase_admin
from firebase_admin import credentials, auth
from app.config import get_settings
import os

settings = get_settings()

def init_fbase():
    if not firebase_admin._apps:
        cred_path = settings.FBASE_CREDENTIALS
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        else:
            print("Warning: Fbase credentials file not found")

def verify_fbase_token(token: str):
    try:
        init_fbase()
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
