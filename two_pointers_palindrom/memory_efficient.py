def isPalindrom(s):
    s = s.lower()
    for c in s:
        if not c.isalnum():
            s = s.replace(c, '')
    return s == s[::-1]

if __name__ == "__main__":
    s = input()
    print(isPalindrom(s))
