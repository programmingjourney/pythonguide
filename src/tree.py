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

    def empty(self):
        return self.size() == 0

class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree_recursively(self):
        print(self.data)

        if self.left != None:
            self.left.print_tree_recursively()
        if self.right != None:
            self.right.print_tree_recursively()

    def print_tree(self):
        q = queue()
        q.enqueue(self)

        while not q.empty():
            front = q.dequeue()
            print(front.data)
            if front.left != None:
                q.enqueue(front.left)
            if front.right != None:
                q.enqueue(front.right)



root = Tree('root')
root.left = Tree('left')
root.right = Tree('right')
root.left.left = Tree('left->left')
root.left.left.left = Tree('left->left->left')
root.left.left.right = Tree('left->left->right')
root.left.left.right.right = Tree('left->left->right->right')
root.left.right = Tree('left->right')

#root.print_tree_recursively()
root.print_tree()