def maxArea(height):
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_area = max(max_area, h * w)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

if __name__ == "__main__":
    height = list(map(int, input().split()))
    print(maxArea(height))
