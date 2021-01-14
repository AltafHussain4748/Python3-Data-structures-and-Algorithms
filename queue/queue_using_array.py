"""Queue implementation using array"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not len(self.queue):
            print("No element in the queue.")
            return
        self.queue.pop(0)

    def is_empty(self):
        if not len(self.queue):
            print("Queue is empty")

    def print_queue(self):
        print(self.queue)


queue = Queue()
queue.is_empty()
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.dequeue()
queue.enqueue(1000)
queue.print_queue()
