n=int(input())
count =0

for i in range(n):
    status= sum(map(int,input().split()))
    if status>=2:
        count+=1
print(count)