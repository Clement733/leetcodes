def topKFrequent(nums, k):
    freq = {}
    for n in nums:
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    return sorted(freq, key=freq.get, reverse=True)[:k]

if __name__ == "__main__":
    k = int(input())
    nums = list(map(int, input().split()))
    print(topKFrequent(nums, k))
