def isValid(s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        close = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in close:
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == "__main__":
    s = input().strip()
    print(isValid(s))
