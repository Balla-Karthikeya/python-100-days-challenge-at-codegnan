<<<<<<< HEAD



import json
try:
    with open('contacts.json','r') as file:
        data =json.load(file)
        print(data)

except Exception as e:
    print(e)


=======

[{
    'name':'Ravi',
    'number':6302722178
},

{
    'name':'raju',
    'number': 9052186454
}]


import json
try:
    with open('contacts.json','r') as file:
        data =json.load(file)
        print(data)

except Exception as e:
    print(e)


>>>>>>> ba4c159c42104fd55ee5e25855b304bff716441d
