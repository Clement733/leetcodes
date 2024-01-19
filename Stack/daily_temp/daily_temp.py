def dailyTemperatures(temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t, i])
        return res

if __name__ == "__main__":
    temperatures = list(map(int, input().split()))
    print(dailyTemperatures(temperatures))
