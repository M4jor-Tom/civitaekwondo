import requests
import logging

from core.constant import mailgun_routes_url
from core.service import KeyManager
from core.util import get_ngrok_url

logger = logging.getLogger(__name__)

class MailgunManager:
    def __init__(self, key_manager: KeyManager):
        self.key_manager: KeyManager = key_manager

    def create_route(self):
        data = {
            'priority': '1',
            'description': 'Forward email content to our server',
            'expression': f'match_recipient(".*@{self.key_manager.mailgun_domain}")',
            'action': [f'forward("{get_ngrok_url()}/parse-email")'],
        }

        # Make the API call to create the route
        response = requests.post(mailgun_routes_url, auth=('api', self.key_manager.mailgun_api_key), data=data)
        print(response.json())

    def delete_routes(self):
        for route_id in self.get_routes_ids():
            self.delete_route_by_id(route_id)

    def get_subscription_url(self) -> str:
        pass

    def get_routes_ids(self) -> list[str]:
        result: list[str] = []
        response = requests.get(mailgun_routes_url, auth=('api', self.key_manager.mailgun_api_key))
        if response.status_code == 200:
            routes = response.json().get("items", [])
            if routes:
                logger.info("Available routes:")
                for route in routes:
                    logger.info(f"Route ID: {route['id']} - Description: {route['description']}")
                    result.append(route['id'])
            else:
                logger.info("No routes found.")
        else:
            logger.error(f"Error listing routes: {response.status_code}, {response.text}")
        return result

    def delete_route_by_id(self, route_id):
        delete_url = f'{mailgun_routes_url}/{route_id}'
        response = requests.delete(delete_url, auth=('api', self.key_manager.mailgun_api_key))
        if response.status_code == 200:
            logger.info(f"Route {route_id} deleted successfully.")
        else:
            logger.error(f"Error deleting route {route_id}: {response.status_code}, {response.text}")
