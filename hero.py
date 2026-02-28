a=input().lower()
# i have to take one string it should be small letter only
# then count the characters and store them dont count repeated character 
# if count is odd print msg that IGNORE HIM! else print CHAT WITH HER!
count =0
seen =set()
for i in a:
    if i not in seen:
        seen.add(i)
        count+=1

if count % 2==0:
    print ("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
