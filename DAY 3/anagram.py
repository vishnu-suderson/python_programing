class solution:
    def groupanagram(self,str):
        reult = {}
        for i in stes: 
         x = "".join(sorted(i))
         if x in reult:
            reult[x].append(i)
        else:
            reult[x] = [i]
            return list(reult.values())

    obi = solution()
    print(ob.groupanagram([]))