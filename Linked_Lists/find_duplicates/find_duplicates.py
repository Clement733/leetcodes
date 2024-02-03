def findDuplicate(nums):
        s = {}
        for n in nums:
            if n not in s:
                s[n] = 0
            s[n] += 1
            if s[n] > 1:
                return n
