class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)
        print(f"Item {item} pushed to stack.")

    def pop(self):
        if not self.queue1:
            print("Stack is empty. Cannot pop.")
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        item = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        print(f"Item {item} popped from stack.")
        return item

    def peek(self):
        if not self.queue1:
            print("Stack is empty.")
            return None
        print(f"Top item is: {self.queue1[-1]}")
        return self.queue1[-1]

    def is_empty(self):
        return len(self.queue1) == 0

    def get_size(self):
        return len(self.queue1)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", list(self.queue1))


