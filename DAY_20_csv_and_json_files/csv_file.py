import csv
try:
    with open('contacts.csv', 'r') as f:
        data=csv.reader(f)
        print(data)
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")

