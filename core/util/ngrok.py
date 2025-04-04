import requests
from core.constant import ngrok_api_url

def get_ngrok_url():
    response = requests.get(ngrok_api_url)
    if response.status_code == 200:
        tunnels: any = response.json().get("tunnels", [])
        if tunnels and len(tunnels) > 0 and "public_url" in tunnels[0]:
            public_url: str = tunnels[0]["public_url"]
            return public_url
        else:
            return "No tunnels found."
    else:
        return "Error connecting to Ngrok API."
