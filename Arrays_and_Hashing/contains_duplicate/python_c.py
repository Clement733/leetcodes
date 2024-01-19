def main(nums):
    return len(set(nums)) == len(nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(main(nums))
