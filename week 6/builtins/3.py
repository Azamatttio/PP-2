def is_palindrome(string):
    reversed_string=''.join(reversed(string))
    if string==reversed_string:
        return True
    else:
        return False
s="radar"
rez=is_palindrome(s)
if rez:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")