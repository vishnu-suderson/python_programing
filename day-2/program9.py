month = input("enter the month:")
day = int(input("enter the day: "))
if month in('january','febuary','march'):
    senson ="winter"
elif month in('april','may','june'):
    senson ="summer"
elif month in('july','august','september'):
    senson ="spring"
else:
    senson="fail"
if (month=="march")and(day>1):
    senson="summer"
if (month=="june")and(day>1):
    senson="spring"
if (month=="septmber")and(day>1):
    senson="fail"
if (month=="december")and(day>1):
    senson="winter"
print("season is ",season)