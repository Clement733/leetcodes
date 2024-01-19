def evalRPN(tokens):
        stack = []
        for e in tokens:
            if e == "+":
                stack.append(stack.pop() + stack.pop())
            elif e == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif e == "*":
                stack.append(stack.pop() * stack.pop())
            elif e == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(e))
        return stack[0]

if __name__ == "__main__":
    tokens = list(map(str, input().split()))
    print(evalRPN(tokens))
