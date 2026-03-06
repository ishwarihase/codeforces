#You are given three integers a, b, and c. Determine if one of them is the sum of the other two.
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a + b == c:
        print("YES")
    elif a + c ==b:
        print("YES")
    elif b + c==a:
        print("YES")
    else:
        print("NO")

    

'''for above we get 4
12 3 4
NO
23 4 5
NO
5 6 4
NO 
this type of output .but we want 
Input
7
1 4 3
2 5 8
9 11 20
0 0 0
20 20 20
4 12 3
15 7 8
Output
YES
NO
YES
YES
NO
NO
YES so'''


