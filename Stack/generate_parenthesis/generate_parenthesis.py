def generateParenthesis(n):
        res = []
        def back(curr, openN, closed):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            if openN < n:
                curr.append("(")
                back(curr, openN + 1, closed)
                curr.pop()
            if closed < openN:
                curr.append(')')
                back(curr, openN, closed + 1)
                curr.pop()
        back([], 0, 0)
        return res

if __name__ == "__main__":
    n = int(input())
    print(generateParenthesis(n))
    print(len(generateParenthesis(n)))
