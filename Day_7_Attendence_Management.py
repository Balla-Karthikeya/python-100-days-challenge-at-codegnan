# Number of students in the class - using for loop 
n=int(input("Enter number of students in the class:"))
present_count=0
absent_count=0
for rollno in range(1,n+1):
    status = input(
        f"Enter student roll number {rollno} status:\n"
        "1. Present\n"
        "2. Absent\n"
        "Enter choice (1 or 2): "
        )
    if status == '1':
        present_count += 1
    elif status == '2':
        absent_count += 1
    else:
        print("Please select either 1 or 2 options")
print("Total students in the class:", n)
print("Number of students present:", present_count)
print("Number of students absent:", absent_count)
percentage=(present_count/n)*100
print("Attendence Report:",percentage)


# Number of students in the class - using while loop
n=int(input("Enter number of students in the class:"))
present_count=0
absent_count=0
rollno = 1 # initilization
while rollno <= n:  # condition
    status = input(
        f"Enter student roll number {rollno} status:\n"
        "1. Present\n"
        "2. Absent\n"
        "Enter choice (1 or 2): "
        )
    if status == '1':
        present_count += 1
        rollno += 1
    elif status == '2':
        absent_count += 1
        rollno += 1
    else:
        print("Please select either 1 or 2 options")
print("Total students in the class:", n)
print("Number of students present:", present_count)
print("Number of students absent:", absent_count)
percentage=(present_count/n)*100
print("Attendence Report:",percentage)
