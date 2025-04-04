from fastapi import APIRouter
from fastapi.params import Depends

from core.provider import get_key_manager
from core.constant import low_layer
from core.service import KeyManager

key_providing_router: APIRouter = APIRouter()

@key_providing_router.get(path="/provide_key", tags=[low_layer])
def provide_key(mailgun_api_key: str, ngrok_auth: str, domain: str, key_manager: KeyManager = Depends(get_key_manager)):
    key_manager.mailgun_api_key = mailgun_api_key
    key_manager.ngrok_auth = ngrok_auth
    key_manager.mailgun_domain = domain
