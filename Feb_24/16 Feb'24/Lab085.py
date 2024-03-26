api_response = {
    "first_name" : "Nitish",
    "age" : 33,
    "last_name" : "Jain", "email": "nitishjain1490@gmail.com",
    "password": "Test123!", "commission" : 10 }
print(api_response)
print(type(api_response))
print(api_response.get("password"))

api_response["password"] = "Check123!"
print(api_response)

for k,v in api_response.items():
    print(k, "=>", v)