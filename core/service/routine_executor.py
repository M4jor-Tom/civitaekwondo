from core.service import SubscriptionUrlGenerator, SubscriptionUrlActivator

class RoutineExecutor:
    def __init__(self, subscription_url_generator: SubscriptionUrlGenerator, subscription_url_activator: SubscriptionUrlActivator):
        self.subscription_url_generator: SubscriptionUrlGenerator = subscription_url_generator
        self.subscription_url_activator: SubscriptionUrlActivator = subscription_url_activator

    async def execute_routine(self):
        subscription_url = await self.subscription_url_generator.generate_subscription_url()
        self.subscription_url_activator.activate_subscription_url(subscription_url)
        return subscription_url
