import pytest
import requests


@pytest.fixture(scope="session")
def postman_request():
    url = "https://api.trello.com/1/members/me/boards?key=c265bc7d9cae5642f069e0bff0dce96d&token=8ece502c8b3fab0541a2a44d0407fa51b9c63687316feccfaa3d76cb2b1dac71"
    payload = {}
    headers = {
        'Cookie': 'dsc=4201ba63b469b212868ff6c87a86d599a6c0ce93dde6cb180120932ece0035d3'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    yield response
