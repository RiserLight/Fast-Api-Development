from passlib.context import CryptContext
password_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash_password(password:str)->CryptContext:
  return password_context.hash(password)

def verify_password(plain_password:str,db_password)->bool:
  return password_context.verify(plain_password,db_password)
