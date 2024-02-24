# Count the number of consonants and vowels in a string

_str = str.lower(input("Enter the string that you want to check: "))
vow = 0
con = 0

for i in _str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vow = vow + 1
    else:
        con = con + 1

print("The number of vowels is : ", vow)
print("The number of consonants is: ", con)