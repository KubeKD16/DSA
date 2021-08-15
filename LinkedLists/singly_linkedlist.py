class SLLNode:
    """ This class initializes the self.data & self.next attributes to a given Node Object of SLLNode class.
    The node object inherits all the below methods which can be used to navigate around in SLL """
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return "SLLNode Data: {}".format(self.data)
    
    def get_data(self):
        """ Returns the self.data attribute of the Node object """
        return self.data
    
    def set_data(self, new_data):
        """ Replaces the self.data attribute of the Node Object with the new_data """
        self.data = new_data

    def set_next(self, new_next):
        """ Replaces the self.next attribute of the Node Object with the new_next Node object """
        self.next = new_next

    def get_next(self):
        """ Returns the self.next attribute of the Node Object"""
        return self.next



class SLL:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return "Head Object data: {}".format(self.head)
    
    def is_empty(self):
        """ Returns true if linkedlist is empty else False """
        return self.head is None

    def add_front(self,new_data):
        """ Adds the new Node object using the new_data attribute to the front of the LinkedList """
        temp = SLLNode(new_data)
        temp.next = self.head 
        self.head = temp
    
    def size(self):
        """ Trraverses the LinkedList and returns the number of Nodes in the SLL. We have to visit each node atleast once
        to check if another Node exists or not. Hence basically, traversing the entire SLL of size N
        The time complexity of this operation is O(N) """
        size = 0
        if self.head is None:
            return 0
        
        current = self.head 
        while current is not None:
            size += 1
            current = current.get_next()
        
        return size

    
    def search(self,data):
        """ Traverses the entire Linked List and checks if the head.data matches with the data we want to search. 
        Worst case, we need to traverse the whole list to check if the data we are searching for does exists. 
        Hence, the time complexity is O(n) where n being the size of the linked List
        """
        if self.head is None:
            return "Linked List is empty. Please insert the node first!"
        
        current = self.head
        while current.get_next() is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        
        return False
    
    def print_list(self):
        current = self.head 
        while current is not None:
            print("{} -> ".format(current))
            current = current.get_next()
        

    def remove(self,data):
        """ Removes the current data node from the Linkedlist that matches the arguement self.head.get_data
        Take O(n) time complexity as in the worst scenario, we will need to traverse the entire SLL to find the data node
        and remove it."""

        if self.head is None:
            return "LL is empty"
        
        current = self.head 
        previous = None
        found = False 
        while not found:
            if current.get_data() == data:
                found = True 
            else:
                if current.get_next() is not None:
                    previous = current
                    current = current.get_next()
                else:
                    return "Node doesn't exist"
        
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


        

        pass 
