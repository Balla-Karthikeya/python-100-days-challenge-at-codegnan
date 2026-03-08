import csv
try:
    with open('students.csv', 'a', newline='') as file:
        fieldnames = ['Roll', 'Name', 'Age', 'Class']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        data = [{'Name': 'abc', 'Age': 11, 'Class': 8},{'Roll': 109, 'Name': 'bca', 'Age': 11, 'Class': 8}]
        writer.writerows(data)
except Exception as e:
    print(e)