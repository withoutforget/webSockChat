import time

from fastapi import APIRouter

from Services import AuthService, MessageService, AuthError
from deps import AuthDep, MessageDep
chat_router = APIRouter(
    prefix = '/chat'
)

@chat_router.post('/{token}/update')
async def update(token: str, authservice : AuthDep, msgservice:MessageDep, after_time:int = 0):
    try:
        user = authservice.validate_token(token)
        return {'ok': 0, 'message': msgservice.get_update(after_time)}
    except AuthError as e:
        return {'ok': 1, 'message': str(e)}
@chat_router.post('/{token}/send')
async def send(token: str, text: str, authservice : AuthDep, msgservice:MessageDep):
    try:
        user = authservice.validate_token(token)
        msgservice.send_message(username=user.username, text=text, timestamp=int(time.time()))
    except AuthError as e:
        return {'ok': 1, 'message': str(e)}