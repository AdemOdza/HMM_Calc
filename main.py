
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Transition properties
    # a[i][j] = probability of traveling to state j from state i
    a = [[0.5, 0.2, 0.3],
         [0.1, 0.6, 0.3],
         [0.2, 0.4, 0.4]]

    # Emission probabilities
    # b[i][x] = Probability of emitting output x at state i
    b = [[0.2, 0.7, 0.1],
         [0.4, 0.4, 0.2],
         [0.7, 0.1, 0.2]]

    # pi[i] = Probability of starting at state i
    pi = [0.5, 0.4, 0.1]

    # Observed output sequence
    sequence = [3, 2, 3]

    alpha = list()

    curr = []
    for i in range(0, len(a[0])):
        var = float(pi[i] * b[i][sequence[0 ] -1])
        curr.append(var)
    alpha.append(curr)

    for x in range(1, len(sequence)):
        curr = []
        for i in range(0, len(a[0])):
            var = 0
            for j in range(0, len(a[0])):
                var += float(a[j][i] * alpha[ x -1][j])
            curr.append(var * b[i][sequence[x] - 1])
        alpha.append(curr)


    for x in range(0, len(alpha)):
        print(f" alpha_t({x})  |", end = "")
    print("\n", "______________ " *len(alpha[0]))
    for x in alpha:
        for y in x:
            print(str(round(y, 6)).center(13), end="|")
        print("\n", "______________ " *len(alpha[0]))
