def editDistance (wordl, word2, m, n): 
    if m== 0: 
        return n
    if n ==0 :
            return m
    if word1 [m-1]== word2 [n-1]:
     return editDistance (wordl, word2, m-1, n-1)
    return 1 + min (editDistance (wordl, word2, m, n-1),editDistance (wordl, word2, m-1, n), editDistance (wordl, word2, m-1, n-1))
word1= input ("Enter a word: ") 
word2=input ("Enter a word: ")
print(editDistance (wordl, word2, len (wordl), len (word2)))