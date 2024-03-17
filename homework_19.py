def is_palindrome(text):
    txt = ''.join(char for char in text if char.isalnum())
    if txt.upper() == txt.upper()[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")