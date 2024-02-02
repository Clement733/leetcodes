def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        sc = s.next
        p = s.next = None
        while sc:
            temp = sc.next
            sc.next = p
            p = sc
            sc = temp
        ft, sc = head, p
        while sc:
            t1, t2 = ft.next, sc.next
            ft.next = sc
            sc.next = t1
            ft, sc = t1, t2
