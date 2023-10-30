import requests
import src.config.config


def test_api():
    print('testing parameters getter')
    response = requests.get(src.config.config.config_all.get("URLTEST"))

    assert response.status_code == src.config.config.config_all.get("response_ok")

    