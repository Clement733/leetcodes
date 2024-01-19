def search(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

if __name__ == "__main__":
    target = int(input())
    nums = list(map(int, input().split()))
    print(search(nums, target))
