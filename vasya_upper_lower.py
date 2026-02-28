s=input()
up=0
low=0
for i in s:
    if i ==i.lower():
        low+=1
    elif i==i.upper():
        up+=1


if up > low:
    print(s.upper())
else:
    print(s.lower())


