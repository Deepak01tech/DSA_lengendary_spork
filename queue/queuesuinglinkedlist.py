class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            # print(f"Node created with data: {data}")
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
        # print("Queue initialized.")
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Item {item} enqueued to queue.")
    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Item {item} dequeued from queue.")
        return item

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        print(f"Front item is: {self.front.data}")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            items = []
            while current:
                items.append(current.data)
                current = current.next
            print("Queue items:", items)
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


