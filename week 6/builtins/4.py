def square_milliseconds(n, milliseconds):
    time.sleep(milliseconds / 1000)
    rez=math.sqrt(n)
    return rez
n=36600
milliseconds=2123
rez=square_milliseconds(n, milliseconds)
print(f"Square root of {n} after {milliseconds} milliseconds is {rez}")