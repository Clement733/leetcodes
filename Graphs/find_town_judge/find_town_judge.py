from collections import defaultdict

def findJudge(n, trust):
        count = defaultdict(int)
        seen = set()
        for a, b in trust:
            count[b] += 1
            seen.add(a)
        for person in range(1, n + 1):
            if count[person] == n - 1 and person not in seen:
                return person
        return -1

if __name__ == "__main__":
    n = int(input("Enter the number of people: "))
    i = int(input("Enter the amount of list(s): "))
    trust = []
    for a in range(i):
        p = list(map(int, input().split()))
        trust.append(p)
    print(findJudge(n, trust))
