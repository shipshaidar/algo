class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        if left:
            self.left.right = self
        if right:
            self.right.left = self


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def _add_between(self, data, lnode, rnode):
        node = Node(data, lnode, rnode)
        if lnode is None:
            self.head = node
        else:
            lnode.right = node
        if rnode is None:
            self.tail = node
        else:
            rnode.left = node
        self._len += 1

    def add_to_head(self, data):
        self._add_between(data, None, self.head)

    def add_to_tail(self, data):
        self._add_between(data, self.tail, None)

    def _rm(self, node):
        if node is self.tail:
            self.tail = node.left
            self.tail.right = None
        elif node is self.head:
            self.head = node.right
            self.head.left = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            node.left = None
            node.right = None
        self._len -= 1
        return node.data

    def pophead(self):
        return self._rm(self.head)

    def pop(self):
        return self._rm(self.tail)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.right

    def _traverse(self, key):
        if key >= len(self):
            raise ValueError("Bad key", key)
        i = 0
        current = self.head
        while i != key:
            current = current.right
            i += 1
        return current

    def __getitem__(self, key):
        return self._traverse(key).data

    def __setitem__(self, key, value):
        self._traverse(key).data = value

    def __delitem__(self, key):
        self._rm(self._traverse(key))

    def __str__(self):
        return "<->".join(str(i) for i in self)

    def __len__(self):
        return self._len
