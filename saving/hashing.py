from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing():
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(plan, hashed):
        return pwd_context.verify(plan, hashed)
