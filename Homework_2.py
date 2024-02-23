num = int(input())
fifth_digit = num % 10
num //= 10
fourth_digit = num % 10
num //= 10
third_digit = num % 10
num //= 10
second_digit = num % 10
num //= 10
first_digit = num
    
reversed_num = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
print(reversed_num)