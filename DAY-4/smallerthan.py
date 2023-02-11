l =[int(i) for i in input().split()]
s = sorted(l)
L = []
for i in l:
    L.append(s.index(i))
print(L)
