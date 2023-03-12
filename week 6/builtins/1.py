def multiply_list(numbers):
    return reduce(lambda x, y: x*y, numbers)
l=list(map(int,input().split()))
rez=multiply_list(l)
print(rez)