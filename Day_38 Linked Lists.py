##Day_38 Linked Lists:


"""
Linked Lists are lists that are not contiguous, instead they contain Nodes, these Nodes contain data and a reference to the next piece of data
"""
class Node:
    """ Node Class represents a Node of the list"""
    def __init__(self, data):
        self.data = data
        self.next = None          # None can also be passed with a default argument in __init__ but this is better for learning. 
        
node1 = Node(5)                 # Instantiating Node 1
node2 = Node(10)                # Instantiating Node 2
node1.next= node2               # Linking 1 -> 2
node3 = Node(15)                # 

node2.next= node3

print(f"node1: {node1}")                                 # 5
print(f"node1.next: {node1.next}")                       # Reference to Next Node
print(f"node1.next.data: {node1.next.data}")             # 10 (Next Nodes Data)
print(f"node1.next.next.data: {node1.next.next.data}\n")   # 15





## LinkedList is another Class which is used to identify where the path begins

class LinkedList:
    """The Linked List represents the beginning of the list"""
    def __init__(self):
        self.head = None                                 # Points to the first node via latter assignment

    def print_list(self):
        """This is a method (function) inside the LinkedList class,  'self' refers to the specific LinkedList object calling this method"""
 
    
        current = self.head                                # 'current' points to the first node in the list, If the list is empty, current will be Non.e
    
        while current is not None:                         # Keep looping as long as 'current' points to an actual node
            print(current.data, end=" → ") # Print current node data, 'end=" → "' means don't go to a new line, just add an arrow. So instead of separate lines, 5 → 10 → 15 → None
            current = current.next                         # Move the 'current' pointer to the next node in the chain
    
        print("None")                                      # After the loop ends, print "None" to show the list has ended

    def append(self,data):  
        """Method for adding Nodes"""                            
        new_node = Node(data)                              # Creates an Instance of Node and stores in the variable new_node

        if self.head is None:                              # If there is no 1st Node
            self.head = new_node                           # Set the new node, as the 1st
            return                                      
        
        current = self.head                                # However, if there is a 1st node, set current to 'self.head' for Node traversal

        while current.next is not None:                    # While there is a next node
            current = current.next                         # Set current variable to the next node

        current.next = new_node                            # Once there are no more nodes, add the new node
        return
    

    def remove(self, value):
        """Method for removing Nodes"""
        if self.head is None:               
            return                                         # Nothing to remove

    # Case 1: Head needs removal
        if self.head.data == value:                        # If the 1st Node (head) is the desired Node
            self.head = self.head.next                     # Override the 1st Node with the 2nd Node
            return

        current = self.head                                # Traversal
        while current.next and current.next.data != value: # While current.next is not empty, and is not the data we want:
            current = current.next                         # Keep traversing

    # Case 2: Found the node to remove
        if current.next and current.next.data == value:                     # If the next node contains the data we want to remove
            current.next = current.next.next               # Omit it, bypassing it
            return

        print(f"The data you are looking to remove is not in the linked list.")
        return


    def length(self):

        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next
        return count
    
    def find(self, val):

        current = self.head
        while current is not None:
            
            print(f"Checking Node with data {current.data}")
            if current.data == val:
                return True
            current = current.next
        return False

linked_list = LinkedList()
for i in [5, 10, 15, 20, 25]:
    linked_list.append(i)
linked_list.print_list()                                   # 5 → 10 → 15 → 20 → 25 → None

linked_list.remove(10)
linked_list.remove(35)
linked_list.print_list()                                   # 5 → 15 → 20 → 25 → None

print(f"\nThe length of the linked list is: {linked_list.length()}\n")
print(linked_list.find(22))





    

    

