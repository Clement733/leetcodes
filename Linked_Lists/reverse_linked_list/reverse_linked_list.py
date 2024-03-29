class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def reverseList(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

def reverseListI(self, head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
