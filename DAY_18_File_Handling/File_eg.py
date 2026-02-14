<<<<<<< HEAD

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
string = " python programming "
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

=======

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

>>>>>>> ba4c159c42104fd55ee5e25855b304bff716441d
