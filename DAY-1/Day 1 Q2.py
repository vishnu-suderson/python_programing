def sumsquare(numbers):
    return [
        sum(map(lambda x: x**2, [i for i in numbers if i%2==1])),
        sum(map(lambda x: x**2, [i for i in numbers if i%2==0]))
    ]
results = sumsquare([18,9,1,12,13,4,30])
print(results)
