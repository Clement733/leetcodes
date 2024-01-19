def trap(height) -> int:
        if not height or len(height) < 3:
            return 0
        vol = 0
        max_l, max_r = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            h_l, h_r = height[l], height[r]
            max_l = max(h_l, max_l)
            max_r = max(h_r, max_r)
            if h_l <= h_r:
                vol += max_l - h_l
                l += 1
            else:
                vol += max_r - h_r
                r -= 1
        return vol


if __name__ == "__main__":
    height = list(map(int, input().split()))
    print(trap(height))
