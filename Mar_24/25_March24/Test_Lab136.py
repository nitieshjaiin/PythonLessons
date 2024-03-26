import allure # pip install allure
import pytest # pip install pytest
import requests # pip install requests

@pytest.mark.crud
@allure.title("Creating Booking - CRUD")
@allure.description("TC #1 - Verify the Create Booking")

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
    firstname = response_json["booking"]["firstname"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert firstname == "Jim"
    assert checkin == "2018-01-01"
    assert booking_id is not None
    assert type(booking_id) == int
    assert booking_id > 0

@pytest.mark.crud
@allure.title("Creating Booking - CRUD")
@allure.description("TC #1 - Verify the Booking is not created with empty data")

def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers = {"Content-Type" : "application/json"}
    payload = {}
    response = requests.post(url=URL,headers=headers,json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))
    assert response.status_code == 500