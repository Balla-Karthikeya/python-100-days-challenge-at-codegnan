
#write mode
"""
f = open('sample.txt', 'w')
string = "hi"
f.write(string) 
f.close()
print("Content added successfully")"""

# append mode
"""
f = open('sample.txt', 'a')
string = " pythonprogramming "
f.write(string) 
f.close()
print("Content added successfully")
"""

# r+mode

f = open('sample.txt', 'r+')
string = "python programming "

f.write(string) 
f.write(' SQL query language')
f.write(' python')
content=f.read()
print(content)
f.close()
print("Content added successfully")

