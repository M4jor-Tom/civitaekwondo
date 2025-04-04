from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from core.config import PROFILE
from core.model import Profile
from core.provider import get_ngrok_manager
from core.rest import routine_router, key_providing_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"🚀 Civitaekwondo is starting with profile [{PROFILE.value}]...")
    yield
    get_ngrok_manager().stop_ngrok_tunnel()

app = FastAPI(lifespan=lifespan)

app.include_router(routine_router)
app.include_router(key_providing_router)

if PROFILE == Profile.DEV:
    from core.rest import subscription_router
    app.include_router(subscription_router)
    from core.rest import test_router
    app.include_router(test_router)
