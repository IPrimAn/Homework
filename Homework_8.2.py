def is_palindrome(text):
    text = text.lower().replace(' ', '')
    text = text.replace('.', '')
    return text == text[::-1]
text = input("Enter word or sentence: ")
if is_palindrome(text):
    print(True)
else:
    print(False)