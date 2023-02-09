def generateparenthis(n):
    result = []
    generateparenthisutill(n,n,"",result)
def generateparenthisutill(left ,right,string,result):
    if left==0 and right==0:
        result.append(string)
        return
    if left > 0:
        generateparenthisutill(left -1, right, string+ "(", result)
    if right < left:    
        generateparenthisutill(left, right-1, string+ ")", result)
if __name__== "__main__":
    n = int(input("enter the number of pairs of parenthid: "))
    result = generateparenthis(n)
    print("all coimbnation of well formed parethiesi are")
    for i in result:
        print(i)
