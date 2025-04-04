from fastapi import APIRouter, Depends

from core.constant import test
from core.provider import get_ngrok_manager, get_civitai_subscriber, get_mailgun_manager
from core.service import NgrokManager, CivitaiSubscriber, MailgunManager

test_router: APIRouter = APIRouter()

@test_router.get(path="/start_stop_ngrok", tags=[test])
def start_stop_ngrok(ngrok_manager: NgrokManager = Depends(get_ngrok_manager)):
    ngrok_manager.start_ngrok_tunnel()
    ngrok_manager.stop_ngrok_tunnel()

@test_router.get(path="/open_tunnel", tags=[test])
async def open_tunnel(
    civitai_subscriber: CivitaiSubscriber = Depends(get_civitai_subscriber),
    mailgun_manager: MailgunManager = Depends(get_mailgun_manager),
    ngrok_manager: NgrokManager = Depends(get_ngrok_manager)
):
    await civitai_subscriber.ready_for_subscription()
    mailgun_manager.delete_routes()
    ngrok_manager.start_ngrok_tunnel()
    mailgun_manager.create_route()
    await civitai_subscriber.subscribe()


@test_router.get(path="/close_tunnel", tags=[test])
async def close_tunnel(
    mailgun_manager: MailgunManager = Depends(get_mailgun_manager),
    ngrok_manager: NgrokManager = Depends(get_ngrok_manager)
):
    result: str = mailgun_manager.get_subscription_url()
    ngrok_manager.stop_ngrok_tunnel()
    mailgun_manager.delete_routes()
    return result
