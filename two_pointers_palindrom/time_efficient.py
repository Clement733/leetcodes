def isPalindrom(s):
    res = ""
    for c in s:
        if c.isalnum():
            res += c.lower()
    return res == res[::-1]

if __name__ == "__main__":
    s = input()
    print(isPalindrom(s))
