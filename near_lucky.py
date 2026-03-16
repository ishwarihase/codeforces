'''the number is lucky if it conrain 4 and 7 but the count of 4 and 7 must be either 4 or 7'''
n=input()
count=0
for i in n:
    if  i== '4' or i=='7' :
        count+=1
        

if count ==4 :
    print("YES")
elif count ==7 :
    print("YES")   
else:
    print( "NO")


