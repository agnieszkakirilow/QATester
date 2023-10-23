import requests
from src.config.config import Config
 

def test_api():
    requests.get(url, timeout = Config.request_timeout)