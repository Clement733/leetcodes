from collections import defaultdict

def validPath(n, edges, source, destination):
        if [source, destination] in edges or [destination, source] in edges:
            return True
        d=defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        vis = set()
        def dfs(i):
            if i == destination:
                return True

            vis.add(i)
            for j in d[i]:
                if j not in vis and dfs(j):
                    return True
            return False
        return dfs(source)

if __name__ == "__main__":
    n = int(input("Number of edges: "))
    edges = []
    for i in range(n):
        edge = list(map(int, input().split()))
        edges.append(edge)
    source, destination = int(input("Starting point: ")), int(input("End point: "))
    print(validPath(n, edges, source, destination))
