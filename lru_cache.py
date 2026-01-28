class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key: Node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        return -1

    
    def put(self, key, value):
        evicted_key = None
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            evicted_key = lru.key
            self._remove(lru)
            del self.cache[lru.key]
    
        return evicted_key



        
    def display(self):
        current = self.head.next
        print("Cache state (Most Recent → Least Recent):")
        while current != self.tail:
            print(f"{current.key}: {current.val}", end="  ")
            current = current.next
        print()
