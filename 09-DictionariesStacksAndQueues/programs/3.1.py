import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
#cards.put('King of Hearts \u2665')    
#cards.put('Queen of Diamonds \u2666')  
#cards.put('Jack of Spades \u2660')   

def cdin(n):
    cards.put(n)

cdin(2)
cdin(3)
cdin(7)
cdin(4)
cdin(1)
cdin(9)
cdin(8)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
sum=0
sum2=0
while not cards.empty():
    card = cards.get()
    print(card)
    if cards.qsize()<2:
        sum+=int(card)
    sum2+=int(card)

print('sum:',sum)
print('sum of rest:',sum2-sum)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
