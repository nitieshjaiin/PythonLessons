import allure
import requests
import pytest

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

def test_put_request():
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


def test_delete():
    try:
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/"
        booking_id = test_create_booking()
        URL = base_url + base_path + str(booking_id)
        cookie = "token=" + test_create_token()
        headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
        }
        print(headers)
        response = requests.delete(url=URL,headers=headers)
        assert response.status_code == 201
    except Exception as e:
        print(e)