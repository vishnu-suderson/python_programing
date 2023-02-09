class solution:
    def lettercobinations(self, digits):
        if (len(digits)==0):
         return[]
        digitchar = {"1": "","2":"abc","3":"def",
        "4":"ghi","5":"jkl0","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":""}
        resus =[""]
        for d in digits:
            tem =[]
            for c in digitchar[d]:
                tem=tem=[r+c for r in  resus]
            resus = tem
            
        return resus
ob = solution()
s = input("enter tthe no\n")
print(ob.lettercobinations(s))
