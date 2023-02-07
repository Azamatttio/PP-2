max = 0
num = 0
a = -1
while a != 0:
    a = int(input())
    if a > max:
        max, num = a, 1
    elif a == max:
        num += 1        
print(num)