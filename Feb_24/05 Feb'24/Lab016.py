name = 'Shaktiman'

print(len(name)) #Length function to find out length of string

# Index starts from 0 whereas length starts 1

print(name[5])
#print(name[9]) #this will result in index error as 9 is out of string range

print(name[len(name)-1])

#string - immutability, i.e. it cannot change the value

str = "Nitiesh"
str = 'Nitish'
print(str)