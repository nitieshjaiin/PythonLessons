import pytest
import requests

@pytest.fixture
def test_create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123",
    }
    response = requests.post(url=url,headers=headers,json=payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token

@pytest.fixture
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL,headers=headers,json=payload)
    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert type(booking_id) == int
    assert booking_id > 0
    return booking_id