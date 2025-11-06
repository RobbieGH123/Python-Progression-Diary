#Introducing Binary Trees and Queues. 

from collections import deque # Deque means Double-Ended Queue, which is faster processed than a list, as changes made to it does not have to be placed onto every item, as it would do in a list.
                              # Also, this is quicker than "import collections" as it doesnt require typing "collections.deque" everytime it is needed.

class TreeNode: # Creates a new object, called TreeNode, as you would when assigning a value to a variable. 
     def __init__(self, val=0, left=None, right=None): # __init__ is a special function, called a constructor, which doesn't require being called like a typical function.
                                                       # The default parameters are executed if it does not receive an input, value = 0, no left or right children. 
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root): # Creating a function, called levelOrder, Parameter root (Top of the tree)

      if not root: # If the tree is empty - meaning it has no route - 
       return []   # Return an empty list. 

      result = [] # Empty list, which we can use to add the nodes into. 

      queue = deque([root])  # Queue is merely a variable, used to track nodes. Deque is what turns it into the Queue, Double Ended. Start with the root node.
      while queue: # Creates a loop, which stays open as long as there are nodes in the queue. 
        level = []  # Store values for this level, creating an individual list for the level itself. 
        for _ in range(len(queue)):  # At the start of the level, it calculates how many nodes are in the current level, therefore knowing when to step, ignoring children notes.
                       node = queue.popleft() # Removes the leftermost node from the queue and assigns it value to the 'Node' Variable which is also a TreeNode object.
                       level.append(node.val) # Adds the value of node, to the list, level.
                       if node.left: # Checks if the TreeNode object variable, Node, has a left child.
                        queue.append(node.left) # If it does, add it to the back of the queue.
                       if node.right: 
                        queue.append(node.right)
        result.append(level) # After running through every Node in the level, it adds the list 'level' to our main list 'result'.
      return result # After the queue is empty, returns the result.

root = TreeNode(1)       # Example using a Simple tree. The root has a value of 1
root.left = TreeNode(2)  # Left child has a value of 2
root.right = TreeNode(3) # Right child has a value of 3

result = levelOrder(root) # Calling the function to test it.
print(result)  # Output should be: [[1], [2, 3]]



           





