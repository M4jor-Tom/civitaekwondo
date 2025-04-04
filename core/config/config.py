from core.config import Env
from core.model import Profile

env = Env()

PROFILE = env.get_profile(Profile.PROD)
APP_PORT = env.get_int("APP_PORT", 8000)
MAIL_PORT = env.get_int("MAIL_PORT", 5000)
LOGGING_LEVEL = env.get("LOGGING_LEVEL", "DEBUG")
