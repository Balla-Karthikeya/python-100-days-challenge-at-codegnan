# writing data into csv files
import csv
try:
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        data = [['106','abc',13,17], ['107','bca',14,9]]
        writer.writerows(data)
        
except Exception as e:
    print(e)