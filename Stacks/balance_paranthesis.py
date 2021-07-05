class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

def match_pairs(input_string):
    pairs = {
        '(':')',
        '{':'}',
        '[':']',
    }

    keys = pairs.keys()
    index = 0
    my_stack = Stack()
    print(my_stack.items)

    while index < len(input_string):
        symbol = input_string[index]

        if symbol in keys:
            my_stack.push(symbol)
        else:
            if my_stack.isEmpty(): return False
            else:
                last_item = my_stack.pop()
                if symbol != pairs[last_item]:
                    return False

        index += 1

    if my_stack.isEmpty(): return True



print(match_pairs('{[()]}'))
print(match_pairs('(([{}]])'))