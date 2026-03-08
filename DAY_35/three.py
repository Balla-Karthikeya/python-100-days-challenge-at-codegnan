# csv file reading as dictionary
import csv
try:
    with open('students.csv', 'r') as file:
        reader=csv.DictReader(file)
        #print(list(reader))
        for row in reader:
            print(row)
except Exception as e:
    print(e)