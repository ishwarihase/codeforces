'''Timur loves codeforces. That's why he has a string s
 having length 10
 made containing only lowercase Latin letters. Timur wants to know how many indices string s
 differs from the string "codeforces".

For example string s=
 "coolforsez" differs from "codeforces" in 4
 indices, shown in bold.

Help Timur by finding the number of indices where string s
 differs from "codeforces".

Note that you can't reorder the characters in the string s.'''


n=int(input())
d="codeforces"
for i in range(n):
    s=input()
    count=0
    for j in range(len(d)):
        if s[j]!=d[j]:
            count+=1
           
    print(count)

                


    

