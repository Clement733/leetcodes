def center(edges, n):
    return list(set(edges[0]) & set(edges[1]))[0]

if __name__ == "__main__":
    n = int(input("Size of main list:"))
    edges = []
    for i in range(n):
        input_str = input("Enter a pair of values (e.g., '1 2'): ")
        values = list(map(int, input_str.split()))
        if len(values) != 2:
            raise ValueError("Invalid input. Please enter exactly two values.")
        edges.append(values)
    print(center(edges, n))
