def findDuplicate(nums):
        s = {}
        for n in nums:
            if n not in s:
                s[n] = 0
            s[n] += 1
            if s[n] > 1:
                return n

def findDuplicate(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            return slow
