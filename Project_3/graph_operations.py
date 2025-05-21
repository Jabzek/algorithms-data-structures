def print_graph(graph, representation, n):
    if representation == "matrix":
        l_matrix = []
        l_matrix.append("  | " + " ".join([str(i) for i in range(1, n+1)]))
        l_matrix.append("--+" + "-" * (n * 2))

        for row in l_matrix:
            print(row)