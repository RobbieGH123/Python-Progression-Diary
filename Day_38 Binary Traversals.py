## Day_39: Binary Traversals

class Node:                       # Node Class

    def __init__(self, value):    # Value Argument
        self.value = value        # Attribute
        self.left = None          # Placeholder for assigning a Left Child, as I saw on Day 38 Linked Lists
        self.right = None         # Placeholder for assigning a Right Child

root = Node('A')                  # Instantiation of Node Class under the Variable 'root'
root.left = Node('B')             # Assign 'B' to the left child of root, which is A
root.right = Node('C')            # Assign 'C' to the right child of root, which is A
root.left.left = Node('D')        # To the left child of 'B' assign D
root.left.right = Node('E')       # To the right child of 'B' assign E
"""
     A
    / \
   B   C
  / \
 D   E
"""

class Traversals:
    def preorder(root):
        if root:                               # Base Case (If the current node exists)
            print(root.value, end=' ')         # Print the current root value, don't go down a line, just add a space.
            Traversals.preorder(root.left)     # Calls preorder on the left child, if there left child is empty, if root is False, then it will try it on the right child.
            Traversals.preorder(root.right)    # For this to to be processed, there cannot be any left child of the current node.

            """START AT A, PRINT A, GO TO B, PRINT B, GO TO D, PRINT D, NO LC, NO RC, BACK TO B, GO TO E, PRINT E, BACK TO A, GO TO C, PRINT C, NO LC, NO RC"""

    def inorder(root):
        if root:                               # Base Case
            Traversals.inorder(root.left)      # Call on the LC, when LC False, go back to the previous iteration
            print(root.value, end=' ')         # When LC False, Prints Node Value
            Traversals.inorder(root.right)     # Call on the RC

            """ START AT A, GO TO B, GO TO D, NO LC, PRINT D, NO RC, BACK TO B, PRINT B, GO TO E, NO LC, PRINT E, NO RC, PRINT A, GO TO C, NO LC, PRINT C, NO RC"""

    def postorder(root):
        if root:                               # Base Case
            Traversals.postorder(root.left)    # Call on LC
            Traversals.postorder(root.right)   # When NO LC, CALL ON RC
            print(root.value, end=' ')         # Print Node Value

            """START AT A, GO TO B, GO TO D, NO LC, NO RC, PRINT D, BACK TO B, GO TO E, NO LC, NO RC, PRINT E, BACK TO A, GO TO C, NO LC NO RC, PRINT C """

    """ITERATIVE TRAVERSAL LOOPS:"""

    def preorder_iterative(root):         
        if not root:                      # If there is no first root (no tree):
            return []                         # Return an empty list
    
        result = []                       # Traversal list, returned at end of Method
        stack = [root]                    # Input the root into the stack, triggering the While Loop.
    
        while stack:                      # If there is a tree, this gets processed
            node = stack.pop()                # Node = Last item in Stack & removes said item, LC processed 1st, if no LC, processes right
            result.append(node.value)           # Process immediately
        
            # Push right first (processed last)
            if node.right:                # If RC:
                stack.append(node.right)      # Add to the 'been here' not traversed necessarily list.
            if node.left:                 # And if RC:
                stack.append(node.left)       # Add to the list too
    
        return result                     # Once every Node is processed, return the Traversal Path.

    
    def inorder_iterative(root): 

        result = []                       # Traversal Path, returned at end of Method
        stack = []                        # Records what we have been to (not added necessarily) in a List.
        current = root                    # Current starts at the Top
    
        while current or stack:           # While there is a Current Node or a value in the list.
            # Go to the leftmost node
            while current:                    # While there is a Current Node:
                stack.append(current)             # Add it to the 'been here' List
                current = current.left            # GO TO LC
        
            # Process the node
            current = stack.pop()             # If current = empty, Reverse, (stack.pop() gives you the last added value in the stack and removes it from stack).
            result.append(current.value)        # Add it to the Traversal List.
        
            # Move to right subtree
            current = current.right          # Move to that Nodes RC, if RC = True, While current: Gets Triggered again.
    
        return result                        # Once all Nodes are processed, return the Traversal List.
    

    def postorder_iterative(root):

        """This works from Reversing the Stack, as RC gets processed before LC, but PostOrder goes LC -> RC -> VISIT"""
        if not root:                         # If there is no tree:
            return []                            # Return an empty list
    
        stack1 = [root]                      # 
        stack2 = []
    
        while stack1:                        # While there are Nodes to be processed
            node = stack1.pop()              # Set 'node' to the Newest Stack Item.
            stack2.append(node)              # Add this 'node' value to Stack2
        
            # Push left then right         
            if node.left:                    # If Current Node has LC:  
                stack1.append(node.left)         # Add it to Stack1
            if node.right:                   # If Current Node has RC:
                stack1.append(node.right)        # Add it to Stack1
    
        # Reverse gives postorder
        return [node.value for node in reversed(stack2)]

print("Pre-order:")
Traversals.preorder(root)
print("\nIn-order:")
Traversals.inorder(root)
print("\nPost-order:")
Traversals.postorder(root)
print(f"\n{'ITERATIVE LOOP OUTPUTS:':^200}\n")
print("Pre-order:")
print(Traversals.preorder_iterative(root))
print("\nIn-order:")
print(Traversals.inorder_iterative(root))
print("\nPost-order:")
print(Traversals.postorder_iterative(root))





                

            

        




