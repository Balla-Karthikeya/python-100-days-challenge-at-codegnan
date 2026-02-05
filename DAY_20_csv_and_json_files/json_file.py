
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


