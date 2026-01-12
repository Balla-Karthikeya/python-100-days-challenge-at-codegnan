# check weather the given number is a positive or negative even, and positive or negative odd
n=int(input())
if n%2==0:
    if n>-1:
        print("Positive Even")
    
    else:
        print("Negative Even")
else:
    if n>1:
        print("Positive Odd")
    else:
        print("Negative Odd")

# check weather which one is even or odd in the given list of number
list=[1,2,3,4,5]
for num in list:
    if num % 2 == 0:
        print("Even number")
    else:
        print("ood number")
print("program done")

# check weather the given number is a positive or negative even, and positive or negative odd using for loop
list=[-1,-2,-3,1,2,3]
for num in list:
    if num%2==0:
        if num>-1:
            print("Positive Even")
        else:
            print("Negative Even")
    else:
        if num>-1:
            print("Positive Odd")
        else:
            print("Negative Odd")

# print num from 1 to 20
for i in range(1,21,1):
    print(i)

# print even number between zero to twenty
for i in range(0,21,2):
    print(i)

# print odd number between one to twenty
for i in range(1,21,2):
    print(i,end=" ")
