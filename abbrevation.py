t = int(input())

for i in range(t):
    word = input()
    
    if len(word) <= 10:
        print(word)
    else:
        count = len(word) - 2
        new_word = word[0] + str(count) + word[-1]
        print(new_word)
