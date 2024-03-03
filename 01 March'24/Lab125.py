try:
    with open("testdata.txt","r") as file: # this is another way of opening a file
        content = file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()