
# Explain All Types of Operators in Python?
# Arthematic operators: + - * / ** % //
# Comparison operators: > < >= <= != ==
# Logical operators: and, or, not
# Bitwise operators: & | ^(xor) >> << ~(2's compliment)
# Assignment operators: +=, -=, *=, /=, //=, **=, %=
# Membership operators: in, not in
# identity operator: is, is not

#-----------------------------------------------------------
"""
Check Even or Odd

Problem:
Given an integer n, check whether the number is Even or Odd.

Test Case 1:
Input: n = 10
Output: Even

Test Case 2:
Input: n = 7
Output: Odd
"""
n = int(input())
if n%2 == 0:
    print("Even")
else:
    print("Odd")
# -----------------------------------------------------------
"""
Find the Largest of Two Numbers

Problem:
Given two integers a and b, print the greater number. If both are equal, print "Equal".

Test Case 1:
Input: a = 12, b = 8
Output: 12

Test Case 2:
Input: a = 5, b = 5
Output: Equal
"""

a = int(input())
b = int(input())

if a > b:
    print(a)
elif a == b:
    print("Equal")
else:
    print(b)

# -------------------------------------------------------------
"""
Check Eligibility to Vote

Problem:
A person is eligible to vote if their age is 18 or above.
Given age, determine eligibility.

Test Case 1:
Input: age = 20
Output: Eligible to vote

Test Case 2:
Input: age = 16
Output: Not eligible to vote
"""

a=int(input())
if a>=18:
    print("Eligible to vote")
else:
    print(" Not eligible to vote")
# ----------------------------------------------------------------
"""
Given marks m, assign grades as follows:

m >= 90 → Grade A
75 <= m < 90 → Grade B
50 <= m < 75 → Grade C
m < 50 → Fail

Test Case 1:
Input: m = 82
Output: Grade B

Test Case 2:
Input: m = 45
Output: Fail
"""
m=int(input())
if m>=90:
    print("Grade A")
elif 75<=m and m<90:
    print("Grade B")
elif 50<=m and m<75:
    print("Grade C")
else:
    print("Fail")

# ------------------------------------------------------------------
"""
Find the Biggest Number Among Three

Statement:
You are given three integers a, b, and c.
Write a program using conditional statements to determine and print the largest number among them.

Test Case 1:

Input:
10 25 15

Output:
25
"""
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)


