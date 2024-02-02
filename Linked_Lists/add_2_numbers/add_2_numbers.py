def addTwoNumbers(l1, l2):
        ans = ListNode(0)
        start = ans
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            head_sum = val1 + val2 + carry
            carry = head_sum // 10
            ans.next = ListNode(head_sum % 10)
            ans = ans.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return(start.next)
