from Models import User
from Repository import Users
import hashlib
import jwt

class AuthError(Exception):
    pass

def hash_password(password:str) -> str:
    return hashlib.sha512(password.encode()).hexdigest()
def create_token(username: str) -> str:
    return jwt.encode(key = 'test_key', payload= {
        'username': username,
    })
def info_from_token(token: str) -> dict:
    return jwt.decode(jwt = token, key = 'test_key')


class AuthService:
    users : Users
    def __init__(self, users:Users):
        self.users = users
    def login(self, username: str, password: str) -> str:
        user = self.users.get_user(username)
        if user is None:
            raise AuthError("User doesn't exist")
        user:User = user
        if user.password != hash_password(password):
            raise AuthError("Invalid user data")
        token = create_token(username)

        return token
    def register(self, username:str, password:str) -> None:
        user = self.users.get_user(username)
        if user is not None:
            raise AuthError("Username has already taken")
        user = User(username = username, password = hash_password(password))
        self.users.set_user(user)
    def validate_token(self, token: str) -> User:
        try:
            data = info_from_token(token)
            return self.users.get_user(data['username'])
        except:
            raise AuthError("Invalid token")