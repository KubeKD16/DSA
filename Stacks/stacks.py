class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """ Accepts item as parameter and appends it to the end of the list
        Returns nothing

        Runtime for this method is O(1) or constant time as appending to the end of the list
        happens in a constant time
        """
        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

    # def __str__(self):
    #     return f'{self.items}'

def main():
    my_stack = Stack()
    my_stack.push('Apple')
    my_stack.items

if __name__ == '__main__': main()
