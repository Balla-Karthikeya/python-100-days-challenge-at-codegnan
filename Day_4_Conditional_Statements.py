# Type function
a=10
print(type(a))

# input functions
num = input()
print(type(num))

num = int(input())
print(type(num), num)

# if number is zero print like "Entered number is zero"
n=int(input())
if n==0:
    print("Entered number is zero")
print("program done")


# check if number is zero or not
num=int(input("Enter a number:"))
if num==0:
    print("Number is zero")
else:
    print("Number is not zero")
# Approach 2
num=int(input("Enter a number:"))
if num!=0:
    print("Number is not zero")
else:
    print("Number is zero")

# check if number is even or odd
a=int(input())
if a%2 == 0:
    print("Number is a even")
else:
    print("Number is odd")

# Positive even, Negative even, Positive odd, Negative odd
a=int(input())
if a>=0 and a%2==0:
    print("Positive even")
elif a<0 and a%2==0:
    print("Negative even")
elif a>=0 and a%2!=0:
    print("Positive odd")
else:
    print("Negative odd")
