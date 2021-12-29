def dyn_matrix(X, xl, Y, yl):
    XY = [[0] * (yl + 1) for _ in range(xl + 1)]
    for x_i, elemX in enumerate(X):
        for y_i, elemY in enumerate(Y):
            if elemX == elemY:
                XY[x_i + 1][y_i + 1] = XY[x_i][y_i] + 1
            else:
                XY[x_i + 1][y_i + 1] = max(XY[x_i + 1][y_i], XY[x_i][y_i + 1])
    return XY

with open('input.txt') as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))
    m = int(f.readline())
    B = list(map(int, f.readline().split()))

C = [[0] * (n + 1) for _ in range(2)]
for elemB in B:
    C[0] = C[1]
    C[1] = [0] * (n + 1)
    for a_i, elemA in enumerate(A):
        if elemA == elemB:
            C[1][a_i + 1] = C[0][a_i] + 1
        else:
            C[1][a_i + 1] = max(C[1][a_i], C[0][a_i + 1])
with open('output.txt', 'w') as f:
    f.write(str(C[-1][-1]))