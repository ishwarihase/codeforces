'''How the snake moves

The snake follows a zig-zag pattern:

✅ Rules:
Row 1 (odd row) → full of #
Row 2 (even row) → only last column has #
Row 3 (odd row) → full of #
Row 4 (even row) → only first column has #
Repeat this pattern...'''


n,m=map(int,input().split())
for i in range(1,n+1):
    if i %2==1:
        print("#" * m)

    else:
        if (i // 2) % 2 == 1:
            print('.' * (m-1) + '#')
        else:
            print('#' + '.' * (m-1))