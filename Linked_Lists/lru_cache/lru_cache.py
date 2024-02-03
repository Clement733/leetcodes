class LRUCache:
    class ListNode:
        def __init__(self, key, val):
            self.val, self.key = val, key
            self.prev, self.next = None, None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head, self.tail = self.ListNode(-1, -1), self.ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    def delNode(self, delNode):
        newprev = delNode.prev
        newnext = delNode.next
        newprev.next = newnext
        newnext.prev = newprev

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.delNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.delNode(curr)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.delNode(self.tail.prev)

        self.addNode(self.ListNode(key, value))
        self.m[key] = self.head.next
