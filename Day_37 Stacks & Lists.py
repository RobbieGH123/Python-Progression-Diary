## Day_37: Stacks & Lists:

print(f"{'STACKS:':^200}\n")

print(f"{'IMPLEMENTING STACKS:':^200}")

class Stack:                                                                 # Initialisation of class to group the Functions of a Stack
    def __init__(self):                                                      # Constructor block
        self.items = []                                                      # Empty List for manipulation

    def push(self, item):                                                    # Push (append)
        self.items.append(item)                                              # Add inputted item to the empty list

    def pop(self):                                                           # Pop (Remove ~ LIFO)
        if not self.is_empty():                                              # If there are elements in the list
            return self.items.pop()                                          # Return the list with the last item removed

    def peek(self):                                                          # Peek (Shows next item to be Popped)
        return self.items[-1] if not self.is_empty() else None               # Return Last Element, if empty return None

    def is_empty(self):                                                      # Checks if empty, returns True or False
        return len(self.items) == 0
    
## STACK TEST AREA:

s1 = Stack()             # Instantiation
print(s1.is_empty())     # True, currently empty
for i in [6, 4, 2, 3]:   # Add to the list
    s1.push(i)
print(s1.peek())         # -> LIFO -> 3
print(s1.is_empty())     # No longer empty, False
print()

#==============================================================================================================================================================================#

print(f"{'IMPLEMENTING QUEUES:':^200}")

class Queue:                                                    # Class Implementation
    def __init__(self):                                         # Constructor
        self.items = []                                         # Empty list for manipulation

    def enqueue(self, item):                                    # Enqueue Method
        self.items.append(item)                                 # Adds to the end

    def dequeue(self):                                          # Dequeue Method
        if not self.is_empty():                                 # If there are elements
            return self.items.pop(0)                            # Return the list, with the item removed from the front

    def peek(self):                                             # Peek Method 
        return self.items[0] if not self.is_empty() else None   # If there are elements -> return the front item

    def is_empty(self):                                         # Checks if Empty Method
        return len(self.items) == 0                             # Return True or False

## LIST TEST AREA:

Q_1 = Queue()
for i in [1, 3, 5 ,7]:
    Q_1.enqueue(i)
Q_1.dequeue()
print(Q_1.items)
print()

#=======================================================================================================================================================================#
"""                                                                                      |
However, list.pop(0) is inefficient as it has to shift every element in the array by -1. |
This therefore leads to the introduction of Double-Ended-Queues (Dequeues)               |
"""                                                                                      
#=======================================================================================================================================================================#
print(f"{'INTRODUCING DEQUE | REBUILDING STACK & QUEUE WITH DEQUE:':^200}\n")

from collections import deque

class Dq_Stack:  
    """
    Due to the nature of Stack Data Structures, Queues typically benefits more from using Deque than Stacks
    """
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    
## Deque Stack Test Area: 

s2 = Dq_Stack()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s2.push(i)
print(s2.container) # -> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
class Dq_Queue:
    """
    .popleft runs in 0(1) whereas .pop(0) takes 0(n) time complexity
    """
    def __init__(self):
        self.container = deque()
    def enqueue(self, val):
        self.container.append(val)
    def dequeue(self):
        return self.container.popleft()
    
## Deque Queue Test Area:

Q2 = Dq_Queue()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i % 2 == 0:
        Q2.enqueue(i)
print(Q2.container)
Q2.dequeue()
print(Q2.container)






