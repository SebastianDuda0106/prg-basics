import queue
cards = queue.LifoQueue()

# adds elements to the top of the stack
n=int(input('Natural number:'))
while n>0:
    if n%2==0:
        cards.put(0)    
    else:
        cards.put(1)  
    n=round(n/2,0)   

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
a=''
while not cards.empty():
    card = cards.get()
    a+=f'{card}'
    print(card)
print('Binary number:',a)