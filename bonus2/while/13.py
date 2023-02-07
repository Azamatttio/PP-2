max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
a = int(input())
while a != 0:
    if a > max1:
        max2, max1 = max1, a
    elif a > max2:
        max2 = a
    a = int(input())
print(max2)