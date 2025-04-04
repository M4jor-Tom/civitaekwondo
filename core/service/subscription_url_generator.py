from core.service import NgrokManager, MailgunManager, CivitaiSubscriber

class SubscriptionUrlGenerator:
    def __init__(self, ngrok_manager: NgrokManager,
                 mailgun_manager: MailgunManager,
                 civitai_subscriber: CivitaiSubscriber):
        self.ngrok_manager: NgrokManager = ngrok_manager
        self.mailgun_manager: MailgunManager = mailgun_manager
        self.civitai_subscriber: CivitaiSubscriber = civitai_subscriber
    async def generate_subscription_url(self):
        await self.civitai_subscriber.ready_for_subscription()
        self.mailgun_manager.delete_routes()
        self.ngrok_manager.start_ngrok_tunnel()
        self.mailgun_manager.create_route()
        await self.civitai_subscriber.subscribe()
        result: str =self.mailgun_manager.get_subscription_url()
        self.ngrok_manager.stop_ngrok_tunnel()
        self.mailgun_manager.delete_routes()
        return result
