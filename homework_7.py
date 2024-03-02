a = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] == 0:                  
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
