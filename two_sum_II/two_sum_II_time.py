def twoSum(numbers, target):
    seen = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement] + 1, index + 1]
        seen[num] = index
    return [0, 0]

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    target = int(input())
    print(twoSum(numbers, target))
