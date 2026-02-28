# Q) antony and danik play chess n times and evertime one won so they want count who win most
# if count of A > count of D then antony won vice versa
n=int(input())
s=input().upper() # no need of upper but not give error after taking it
count_anton=0
count_danik=0
for i in s:
    if i=='A': # ishwari remember u take here A gives error bcz A treated as varibale which is not declared so u have to take as 'A'
        count_anton+=1
        
    if i=='D':
        count_danik+=1

if count_anton > count_danik :
    print("Anton")

elif count_anton < count_danik:
    print("Danik")

else:
    print("Friendship")






