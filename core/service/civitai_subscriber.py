import asyncio

class CivitaiSubscriber:
    async def ready_for_subscription(self):
        asyncio.create_task(self.init_browser())
        await self.open_browser()
        await self.fill_email_input()
    async def subscribe(self):
        await self.click_subscribe()
        await self.shutdown_browser()

    async def init_browser(self):
        pass
    async def open_browser(self):
        pass
    async def shutdown_browser(self):
        pass
    async def fill_email_input(self):
        pass
    async def click_subscribe(self):
        pass
