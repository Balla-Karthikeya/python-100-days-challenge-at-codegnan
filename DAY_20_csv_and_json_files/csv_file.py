<<<<<<< HEAD
import csv
try:
    with open('contacts.csv', 'r') as f:
        data=csv.reader(f)
        print(data)
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")

=======
import csv
try:
    with open('contacts.csv', 'r') as f:
        data=csv.reader(f)
        print(data)
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")

>>>>>>> ba4c159c42104fd55ee5e25855b304bff716441d
