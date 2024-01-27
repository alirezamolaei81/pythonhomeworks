a = list((input() .split()))
a.sort(key=lambda x: int(x[1:]))
for i in range (len(a)):
    a[i] = a[i][0]

print("".join(a))