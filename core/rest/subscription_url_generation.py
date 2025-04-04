from fastapi import APIRouter, Depends

from core.constant import low_layer
from core.provider import get_subscription_url_generator
from core.service import SubscriptionUrlGenerator

subscription_router: APIRouter = APIRouter()

@subscription_router.get(path="/generate_subscription_url", tags=[low_layer])
def generate_subscription_url(subscription_url_generator: SubscriptionUrlGenerator = Depends(get_subscription_url_generator)):
    subscription_url_generator.generate_subscription_url()
