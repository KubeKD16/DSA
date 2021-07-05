class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """ adds an item to the 0th element of the list that is representing the Queue
        Insertion takes O(n) time (linear time) as every time an element is added to the 0th index of the
        list, it forces the other elements in the list to move right by one index
        """
        self.items.insert(0,item)

    def dequeue(self):
        """ Returns and removes the last item from the list which happens to be the right most item
        in the Queue
        Deletion of the element takes O(1) constant time as you always remove the last item from the list
        which happens to be the right-most element in the queue

        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """ returns the last element in the list which represents the front-most item in the Queue
        Peek takes O(1) constant time as we are just indexing to the last item of the list and returning
        the value from there """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """ returns the size of the Queue which happens to be the length of the list
        Takes O(1) constant time as we are simply returning the length of the list """
        return len(self.items)

    def is_empty(self):
        """ Returns boolean value whether there's an item in the list or element in the queue
        Constant time O(1) as we check only for equality """
        return self.items == []
