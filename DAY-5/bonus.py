grade=input("enter the grade in capes:")
salary= int(input("enter the annual income:"))
if(salary<=0):
    bonus=0
    print("enter corect one")
elif grade=="A":
    if salary<10000:
        bonus = salary*(7/100)
        bonus_in= bonus + salary
        print(bonus_in)
    else:
        bonus = salary*(5/100)
        bonus_in = bonus + salary
        print(bonus_in)
    
elif grade=="B":
    if salary<10000:
        bonus = salary*(12/100)
        bonus_in= bonus + salary
        print(bonus_in)
    else:
        bonus = salary*(10/100)
        bonus_in = bonus + salary
        print(bonus_in)