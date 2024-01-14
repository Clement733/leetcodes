def longestConsecutive(nums) -> int:
        nums = sorted(set(nums))
        result = []
        current = []
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1] + 1:
                result.append(current)
                current = []
            current.append(nums[i])
        result.append(current)
        max_length = max(len(streak) for streak in result)
        return max_length

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(longestConsecutive(nums))
