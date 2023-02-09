time = int(input("Enter the number of time slots:"))
entry = [int(input("enter the number of guests are entering at time slot|{}: ".format(i+1))) for i in range(time) ]
exit = [int(input("enter the number of guests are exiting at time slot{}: ".format(i+1))) for i in range(time)]

count = 0
guests = []
for i in range(len(entry)):
    count = count+entry[i]-exit[i]
    guests.append(count)

print("the maximum number of guests present at any time:", max(guests))
