def count_up_low(string):
    up_count=0
    low_count=0
    for char in string:
        if char.isupper():
            up_count+=1
        elif char.islower():
            low_count+=1
    return (up_count,low_count)
s="Hello my name is Azamat"
rez=count_up_low(s)
print(rez)