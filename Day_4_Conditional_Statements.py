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

# check num is positive, negative or zero
a=int(input())
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

# Find Biggest num of three numbers 
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print("a is the biggest number")
elif b>=a and b>=c:
    print("b is the biggest number")
else:
    print("c is the biggest number")

# check weather num is 5's factor or not
n = int(input("enter a number: "))
if n % 5 == 0:
    print("given number is a factor of 5")
else:
    print("given number is not a factor of 5")

# check weather num is factor of 3 and 5, factor of 5, factor of 3 not a factor of 3 and 5
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print("given number is a factor of 3 and 5")
elif a % 5 == 0:
    print("given number is a factor of 5")
elif a % 3 == 0:
    print("given number is a factor of 3")
else:
    print("given number is not a factor of 3 and 5")



