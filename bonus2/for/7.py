a = int(input())
sum = 1
rez = 0
for i in range(1, a+1):
    sum *= i
    rez += sum
print(sum)