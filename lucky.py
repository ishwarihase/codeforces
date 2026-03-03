#A ticket is a string consisting of six digits. A ticket is considered lucky if the sum of the first three digits is equal to the sum of the last three digits. Given a ticket, output if it is lucky or not. Note that a ticket can have leading zeroes
n=int(input())
result=[]
for i in range(n):
    s=input()
    

    first=int(s[0])+int(s[1])+int(s[2])
    second=int(s[3])+int(s[4])+int(s[5])
    if(first==second):
        result.append("YES")
    else:   
        result.append("NO")

for r in result:
    print(r)

        