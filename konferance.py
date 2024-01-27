
n = int(input())

mail= []
for i in range(n):
    mail.append(input())

a = set()
for email in mail:
    for i in range(len(email)):
        if email[i] == '@':
            a.add(email[i+1:])
            break

a = sorted(a)
for i in a:
    print(i)