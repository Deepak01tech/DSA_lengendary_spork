from collections import deque
class stack:
    def __init__(self):

        self.deque = deque()

    def push(self, item):
        self.deque.append(item)
        print(f"Item {item} pushed to stack.")

    def pop(self):
        if not self.deque:
            print("Stack is empty. Cannot pop.")
            return None
        item = self.deque.pop()
        print(f"Item {item} popped from stack.")
        return item

    def peek(self):
        if not self.deque:
            print("Stack is empty.")
            return None
        print(f"Top item is: {self.deque[-1]}")
        return self.deque[-1]

    def is_empty(self):
        return len(self.deque) == 0

    def get_size(self):
        return len(self.deque)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", list(self.deque))