def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        t = numbers[l] + numbers[r]
        if t > target:
            r -= 1
        elif t < target:
            l += 1
        else:
            return [l + 1, r + 1]

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    target = int(input())
    print(twoSum(numbers, target))
