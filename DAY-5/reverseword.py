class Solution:
    def reverseWords(self, s: str) -> str:
        lists = s.split(" ")[::-1]
        newlists = [x for x in lists if x != '']
        
        return " ".join(newlists)
x = Solution()
s = input("enter the words:")
print(x.reverseWords(s))