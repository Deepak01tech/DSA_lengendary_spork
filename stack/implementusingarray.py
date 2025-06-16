class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Item {item} pushed to stack.")

    def pop(self):
        if not self.items:
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop()
        print(f"Item {item} popped from stack.")
        return item

    def peek(self):
        if not self.items:
            print("Stack is empty.")
            return None
        print(f"Top item is: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()
    print("Is stack empty?", stack.is_empty())
    print("Stack size:", stack.get_size())
    stack.pop()
    stack.pop()
    stack.pop()  # Attempt to pop from an empty stack
    stack.display()  # Display after popping all items
