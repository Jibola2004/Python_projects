from firebase import db
from fastapi import HTTPException, status
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Firebase collection to store users
users_ref = db.collection('users')

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def register_user(email: str, username: str, password: str):
    # Check if the username already exists in Firestore
    user_doc = users_ref.document(username).get()
    if user_doc.exists:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password before storing it
    hashed = get_password_hash(password)
    
    # Add user to Firebase Firestore
    user_data = {
        "email": email,
        "username": username,
        "password": hashed
    }
    users_ref.document(username).set(user_data)

def authenticate_user(username: str, password: str):
    # Retrieve the user from Firestore
    user_doc = users_ref.document(username).get()
    if not user_doc.exists:
        return False  # User not found

    # Get the hashed password from the document
    stored_password = user_doc.to_dict().get('password')
    
    # Verify the password
    return verify_password(password, stored_password)
