# pangram means all 26 letters

n= int(input())
b=input().lower()
unique=set()
for i in b:
    unique.add(i)

if len(unique)==26:
    print("YES")
else:
    print("NO")











