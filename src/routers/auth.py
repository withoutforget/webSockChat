from fastapi import APIRouter

from src.deps import AuthDep
from src.services.auth import AuthError

auth_router = APIRouter(
    prefix='/auth'
)


@auth_router.post('/login')
async def login(username: str, password: str, authservice: AuthDep):
    try:
        token = authservice.login(username, password)
        return {'ok': 0, 'token': token}
    except AuthError as e:
        return {'ok': 1, 'message': str(e)}


@auth_router.post('/register')
async def register(username: str, password: str, authservice: AuthDep):
    try:
        authservice.register(username, password)
        return {'ok': 0, 'message': 'Registered'}
    except AuthError as e:
        return {'ok': 1, 'message': str(e)}
