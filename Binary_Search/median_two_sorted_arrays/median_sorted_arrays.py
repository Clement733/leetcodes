def findMedianSortedArrays(nums1, nums2):
        median = 0
        merged_arr = sorted(nums1 + nums2)
        if len(merged_arr) % 2 == 0:
            num1 = merged_arr[round(len(merged_arr)/2)]
            num2 = merged_arr[round(len(merged_arr)/2) - 1]
            median = (num1 + num2) / 2
        else:
            median = merged_arr[len(merged_arr)//2]
        return median

if __name__ == "__main__":
    nums1, nums2 = list(map(int, input().split())), list(map(int, input().split()))
    print(findMedianSortedArrays(nums1, nums2))
