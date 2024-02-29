
while True:
    first_number = int(input("Please enter first number:"))
    second_number = int(input("Please enter second number:"))
    sign = input("Please enter action:")
    if second_number == 0 and sign == "/":
        print("You can't divide by 0")
    else:
        if sign == "/":
            print('Your result is', int(first_number / second_number))
        if sign == "*":
            print('Your result is', first_number * second_number)
        if sign == "+":
            print('Your result is', first_number + second_number)
        if sign == "-":
            print('Your result is', first_number - second_number)
        quest = input('If you want to perform another calculation, print: "y"')
    if quest.lower() == 'y':
        continue
    else:
        break