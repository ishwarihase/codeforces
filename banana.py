'''A soldier wants to buy w bananas in the shop. 
He has to pay k dollars for the first banana, 2k dollars for the second one and so on 
(in other words, he has to pay i·k dollars for the i-th banana).
He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?
'''
k ,n ,w = map(int,input().split())
amount=0
price=0
for i in range(1 , w+1):
    amount+= i*k
    price=amount-n

if price < 0: 
    price=0
print(price)