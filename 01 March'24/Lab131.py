import csv

test_data = [
    ['Name', 'City', 'Age'],
    ['Nitish', 'HYD', 33],
    ['Nitiesh', 'SMQL', 34],
]

try:
    with open('mydata.csv', 'w') as file:
        writer = csv.writer(file)
        for data in test_data:
            writer.writerow(data)
except FileNotFoundError as f:
    print(f)
finally:
    file.close()
    print("Close the file")
