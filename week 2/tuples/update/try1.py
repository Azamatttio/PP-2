x = ("banana", "apple", "mango")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)