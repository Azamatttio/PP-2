import re
with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding='utf-8') as file:
    content= file.read()
result=re.findall("^[A-Z][a-z]+",content)
print(result)