def calculator(self,s):
    s = s.replace(" ","")
    pn = [1 if c=="+" else-1 for c in s if c in "+"]
    slist =[self.cal(c) for c in s.replace("-","+").split("+")]
    return  slist[0] + sum ([slist[i+1]*pn[i] for i in xrange(len(pn))])
def cal(self,s):
    if "*"not in s  and "/" not in s:
        return int(s)