import subprocess
import time
import logging

from core.config import MAIL_PORT
from core.service import KeyManager

logger = logging.getLogger(__name__)

class NgrokManager:
    ngrok_process: subprocess.Popen | None = None

    def __init__(self, key_manager: KeyManager):
        self.key_manager: KeyManager = key_manager

    def start_ngrok_tunnel(self):
        self.ngrok_process = subprocess.Popen(['ngrok', 'http', str(MAIL_PORT)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f"Ngrok started on port {MAIL_PORT}")
        time.sleep(3)

    def stop_ngrok_tunnel(self):
        self.ngrok_process.terminate()
        logger.info(f"Ngrok from port {MAIL_PORT} stopped")
