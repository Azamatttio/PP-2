n = int(input())
a = 2
power = 1
while a <= n:
    a *= 2
    power += 1
print(power - 1, a // 2)