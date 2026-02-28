s1= input()
s2=input()
s1=s1.lower()
s2=s2.lower()

for i in range(len(s1)):
    if s1[i]>s2[i]:
            print(1)
            break
    elif s2[i]>s1[i]:
          
          print(-1)
          break
else:
          print(0)