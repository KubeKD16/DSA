class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """ inserting at the front of the list which we add at the 0th index of the list
        Insertion takes linear time O(n) time as we insert always at the start of the list, all the
        other items in the list need to shift 1 element right"""
        self.items.insert(0,item)

    def add_rear(self, item):
        """ adds the item to the last index of the list. Normal append operation that adds the item
        to the last index of the list. Insertion takes O(1) time as we always add the item to the last index
        of the list
        """
        self.items.append(item)

    def remove_front(self):
        """ Remove and return the item at the 0th index of the list. The runtime is also in linear time O(n)
        as the remaining elements need to shift left in the list
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """ Removes and returns the last item (right-most) of the list which represents the
        
        rear of the deque. The runtime is O(1) time as it's a constant time
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """ returns the first item in the list which represents the front of the deque.
        Constant runtime of O(1) as we are simply returning the first item from left of the list """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """ returns the last item in the list which represents the rear of the deque. Constant runtime of
        O(1) as we are simply returning the last value in the list from right """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
