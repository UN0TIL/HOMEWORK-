second = int(input())
minutes = 0
hours = 0
days = 0
text = "днів"

if second > 59:
    minutes, second = divmod(second, 60)
if minutes >= 60:
    hours, minutes = divmod(minutes, 60)
if hours >= 24:
    days, hours = divmod(hours, 24)

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if second < 10:
    second = '0' + str(second)

if int(str(days)[-1]) in {0, 5, 6, 7, 8, 9} or int(str(days)[-2:]) == 14:
    text = "днів"
elif int(str(days)[-1]) in {2, 3, 4}:
    text = "дні"
if int(str(days)[-1]) == 1:
    text = "день"


print(f"{days} {text}, {hours}:{minutes}:{second}")
