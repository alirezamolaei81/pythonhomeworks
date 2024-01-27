nums = input() .split()
sum = int(input())

dic = {}
ans = []

for i , num in enumerate(nums):
    num = int(num)
    next = sum - num

    if(next in dic) :
        ans.append(dic[next]+i)
    else:
        dic[num]= i

ans.sort()

if ans==[] :
    print("Not Found!")
else:
    for i in ans:
        print(i)