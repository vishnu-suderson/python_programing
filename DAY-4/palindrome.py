s = input()
s = s.lower()

d = ""
for i in s:
    if(i!=i.isalpha()):
        continue
    else:
        d +=1
st=""
for i in s:
    if(i != i.isalpha()):
        continue
    else:
        st =st+i
if (d==st[::-1]):
    print("true")
else:
    print("false")