
phone_book = {"Nitish": 33, "Jain": 42,"Nitiesh": 24, "Jaiin": 6}
print(len(phone_book))

print(phone_book["Nitish"])
print(phone_book["Jaiin"])

pho_boo = dict(Nitish=33, Jain=24, Nitiesh=42, Jaiin=6)
print(pho_boo)
print(pho_boo['Jaiin'])
print(pho_boo["Jain"])
print(pho_boo.get('Nitish'))
print(pho_boo.get("Nitiesh"))

details = {"Nitiesh": 34, "33": 42, "NJ": 15}
print(details.get("33"))


my_dict = {'a': 1, 'b':6, 'e':4, 'a':8}

print(len(my_dict))