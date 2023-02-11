total = int(input("enter total number of users"))
staff = int(input("Enter total number of staff users"))
non_teaching=staff/3
student_users = total-(staff+non_teaching)
if student_users<=0:
     print("student users: 0 (or) no users")
else:
    print("student users:",student_users)
