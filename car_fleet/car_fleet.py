def carFleet(target, position, speed):
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(cars)[::-1]:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    target = int(input())
    position, speed = list(map(int, input().split())), list(map(int, input().split()))
    print(carFleet(target, position, speed))
