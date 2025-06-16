class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Item {item} enqueued to queue.")

    def dequeue(self):
        if not self.items:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.items.pop(0)
        print(f"Item {item} dequeued from queue.")
        return item

    def peek(self):
        if not self.items:
            print("Queue is empty.")
            return None
        print(f"Front item is: {self.items[0]}")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue items:", self.items)

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    queue.peek()
    queue.dequeue()
    queue.display()
    print("Is queue empty?", queue.is_empty())
    print("Queue size:", queue.get_size())
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()  # Attempt to dequeue from an empty queue
    queue.display()  # Display after dequeuing all items
