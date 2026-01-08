#Integer to another type
a=10
print(float(a))
print(str(a))
print(bool(a))
a=0
print(bool(a))
#Float to another type
a=10.25
print(int(a))
print(str(a))
#String to another type
a="1025"
print(int(a))
print(float(a))
# "3.56" - int
a="3.56"
print(int(float(a)))
#string to list, tuple, set
a="hi"
print(list(a))
print(tuple(a))
print(set(a))
#list to another type
a=[1,2,3,3]
print(set(a))
print(tuple(a))
#Tuple to another type
t=(1,2,3,4,1)
print(set(t))
print(list(t))

