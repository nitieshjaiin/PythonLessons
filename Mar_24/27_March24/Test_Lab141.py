import pytest
import requests
from conftest import test_create_token, test_create_booking
def test_put_request(test_create_token, test_create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = test_create_booking()
    URL = base_url+base_path+str(param)
    cookie = "token=" + test_create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(headers)
    payload = {
           "firstname": "Nitish",
            "lastname": "Jain",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    response = requests.put(url=URL,headers=headers,json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Nitish", "Failed Message - Incorrect First Name"
