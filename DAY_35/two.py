import csv
try:
    with open('students.csv', 'r') as file:
        reader=csv.reader(file)
        #print(list(reader))
        for row in reader:
            print(row)
except Exception as e:
    print(e)