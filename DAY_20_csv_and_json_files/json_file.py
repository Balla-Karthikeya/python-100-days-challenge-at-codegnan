


import json
try:
    with open('contacts.json','r') as file:
        data =json.load(file)
        print(data)

except Exception as e:
    print(e)


