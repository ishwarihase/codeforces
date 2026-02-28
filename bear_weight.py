c,d =map (int,input().split())
count=0
while c<=d:
    c=c*3 
    d=d*2
    count+=1

if c>d:
    print(count)