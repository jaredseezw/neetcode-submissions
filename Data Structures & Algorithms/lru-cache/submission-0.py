class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    #Helpers - Remove and insert in doubly-linked list
    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def insert(self, node):
        temp = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = temp
        temp.next = node 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}
        self.left = self.Node(0, 0) #least-recent end
        self.right = self.Node(0, 0) #most-recent end
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.hashtable:
            return -1
        else:
            self.remove(self.hashtable[key])
            self.insert(self.hashtable[key])
            return self.hashtable[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return 
        
        node = self.Node(key, value)
        self.hashtable[key] = node
        self.insert(node)

        if len(self.hashtable) > self.capacity:
            oldest = self.left.next
            self.remove(oldest)
            del self.hashtable[oldest.key]
