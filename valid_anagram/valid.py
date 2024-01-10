def main(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s, t = input(), input()
    print(main(s, t))
