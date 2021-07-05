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
        in the Queue"""
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        pass

    def size(self):
        return len(self.items)

    def is_empty(self):
        pass
