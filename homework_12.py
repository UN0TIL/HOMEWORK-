from string import punctuation

text = input("Введи текст: ")
text = text.title()
text = text.replace(" ", "")
text = ''.join(char for char in text if char not in punctuation)
if len(text) > 140:
    x = len(text) - 139
    text = text[:-x]
print("#" + text)