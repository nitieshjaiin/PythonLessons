with open("ted.txt",'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line)
    file.close()

with open("ted.txt", 'a') as file:
    file.write("\n This is appending the file")