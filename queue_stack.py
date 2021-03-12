class stack:
    # Constructs an empty list
    def __init__(self):
        self.stack = []

    # Gives the last element of the list
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop() # self.stack[-1]

    # Inserts an element to the end of the list
    def push(self, item):
        self.stack.append(item)

    # Returns the length of the list
    def size(self):
        return len(self.stack)

class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0) # self.queue[0] del self.queue[0]

    def size(self):
        return len(self.queue)