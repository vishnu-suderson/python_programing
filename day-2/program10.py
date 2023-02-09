import operator as op
def removrcommonwords(sent1,sent2):
    com =[]
    sent1 = list(sentence1.split())
    sent2 = list(sentence2.spilt())
    for i in sent1:
        if op.countof(sent2,i)>0:
            sent1.remove(i)
            sent2.remove(i)
    print(*sent1)
    print(*sent2)
    return

sentence1 = input("enter")
sentence2 = input(" enter")
removrcommonwords(sentences1, sentences2)    