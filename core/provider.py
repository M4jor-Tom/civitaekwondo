from functools import lru_cache
from core.service import KeyManager, NgrokManager, MailgunManager, SubscriptionUrlGenerator, CivitaiSubscriber, \
    SubscriptionUrlActivator
from core.service.routine_executor import RoutineExecutor


@lru_cache
def get_key_manager() -> KeyManager:
    return KeyManager()

@lru_cache
def get_ngrok_manager() -> NgrokManager:
    return NgrokManager(get_key_manager())

@lru_cache
def get_mailgun_manager() -> MailgunManager:
    return MailgunManager(get_key_manager())

@lru_cache
def get_civitai_subscriber() -> CivitaiSubscriber:
    return CivitaiSubscriber()

@lru_cache
def get_subscription_url_generator() -> SubscriptionUrlGenerator:
    return SubscriptionUrlGenerator(get_ngrok_manager(), get_mailgun_manager(), get_civitai_subscriber())

@lru_cache
def get_subscription_url_activator() -> SubscriptionUrlActivator:
    return SubscriptionUrlActivator()

@lru_cache
def get_routine_executor() -> RoutineExecutor:
    return RoutineExecutor(get_subscription_url_generator(), get_subscription_url_activator())
