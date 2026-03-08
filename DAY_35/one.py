import csv
try:
    with open('students.csv', 'r') as file:
        reader=csv.reader(file)
        print(list(reader))
except Exception as e:
    print(e)