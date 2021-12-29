with open('input.txt') as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))
    m = int(f.readline())
    B = list(map(int, f.readline().split()))
    l = int(f.readline())
    C = list(map(int, f.readline().split()))

D = [[[0 for i in range(l+1)] for j in range(m+1)] for k in range(n+1)]
for a_i, elemA in enumerate(A):
    for b_i, elemB in enumerate(B):
        for c_i, elemC in enumerate(C):
            if elemA == elemB and elemB == elemC:
                D[a_i + 1][b_i + 1][c_i + 1] = D[a_i][b_i][c_i] + 1
            else:
                D[a_i + 1][b_i + 1][c_i + 1] = max(D[a_i + 1][b_i + 1][c_i],
                                                   D[a_i + 1][b_i][c_i + 1],
                                                   D[a_i][b_i + 1][c_i + 1])
with open('output.txt', 'w') as f:
    f.write(str(D[-1][-1][-1]))