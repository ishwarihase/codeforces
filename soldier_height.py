'''we want to make sure that first number in list is largest and last number is lowest if not then count how much swap is required to make list like this'''
n=int(input())
num=list(map(int,input().split()))
# first num large than other and last num is smaller than each
'''for i in range(num1):
    if arr[i]<=arr[i+1]:
        count+=1
        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp'''
# find lagrest numa dn index and smallest num and index
b=max(num)
indx_max=num.index(b)
d=min(num)
indx_min=len(num)-1 - num[::-1].index(d) #smallest and also not first occurance we want lasst occurance so use this


# now we want to search how many swaps ar required



# swaps needed
steps = indx_max + (n - 1 - indx_min)

# adjustment
if indx_max < indx_min:
    steps -= 1

print(steps)



















'''for i in num:
    if num[0]>=num[0:]:
        count=0
    else:

    if num[len(num)-1]<=num[:0]:'''

        





