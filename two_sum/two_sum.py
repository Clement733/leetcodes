def twoSum(nums, target: int):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return []

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    print(twoSum(nums, target))
