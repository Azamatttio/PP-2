def str(remaining,candidate=' '):
    if len(remaining)==0:
        print(candidate)
    for i in range(len(remaining)):
        newcan=candidate+remaining[i]
        newrem=remaining[0:i]+remaining[i+1:]
        str(newrem,newcan)
if __name__=='main':
    s=input()
    str(s)
s=input()
str(s)