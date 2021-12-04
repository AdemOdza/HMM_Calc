

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [[0.5, 0.2, 0.3],
         [0.1, 0.6, 0.3],
         [0.2, 0.4, 0.4]]

    b = [[0.2, 0.7, 0.1],
         [0.4, 0.4, 0.2],
         [0.7, 0.1, 0.2]]

    pi = [0.5, 0.4, 0.1]
    sequence = [3,2,3]

    alpha = list()

    curr = []
    for i in range(0, len(a[0])):
        var = float(pi[i] * b[i][sequence[0]-1])
        curr.append(var)
    alpha.append(curr)

    for x in range(1, len(sequence)):
        curr = []
        for i in range(0, len(a[0])):
            var = 0
            for j in range(0, len(a[0])):
                var += float(a[j][i] * alpha[x-1][j])
            curr.append(var*b[i][sequence[x] - 1])
        alpha.append(curr)


    for x in range(0, len(alpha)):
        print(f" alpha_t({x}) |", end = "|")
    print("\n", "______________"*len(alpha[0]))
    for x in alpha:
        for y in x:
            print(str(round(y, 6)).center(13), end="|")
        print("\n", "______________"*len(alpha[0]))


