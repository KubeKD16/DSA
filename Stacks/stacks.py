class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """ Accepts item as parameter and appends it to the end of the list.Returns nothing

        Runtime for this method is O(1) or constant time as appending to the end of the list
        happens in a constant time
        """
        self.items.append(item)

    def pop(self):
        """Returns and Removes the last item from the list which is also the top item of the Stack.

        Runtime is also constant time O(1) as we are indexing the last item of the list
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """ This method returns the last item in the list, which also happens to be the top item in the Stack

        Runtime is constant O(1) as the indexing into a list is done in constant time """

        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """ Returns the length of the list that represents the stack
        Runtime is constant time O(1) because finding the length of the list also happens in constant time"""

        return len(self.items)

    def is_empty(self):
        """ Returns a boolean value describing whether or not the stack is Empty
         The test of equality below happens in constant time O(1)
        """
        return self.items == []

    # def __str__(self):
    #     return f'{self.items}'

def main():
    my_stack = Stack()
    my_stack.push('Apple')
    my_stack.items

if __name__ == '__main__': main()
