def alibaba(N, M, R: list):
    cash = 0
    for i in range(M):
        cash += R.pop(R.index(max(R)))
    return cash


print(alibaba(4, 2, [0, 3,-1,-2]))
