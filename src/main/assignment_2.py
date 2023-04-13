
import numpy as np

from scipy.linalg import solve

#1
def nevilles_method(x, y, xadv):

    size = len(x)

    matrix = np.zeros((size, size))

    for index, row in enumerate(matrix):

        row[0] = y[index]
    
    numbs = len(x)

    for i in range(1, numbs):

        for j in range(1, i + 1):

            multione = (xadv - x[i - j]) * matrix[i][j - 1]

            multitwo = (xadv - x[i]) * matrix[i - 1][j - 1]

            div = x[i] - x[i - j]

            frac = (multione - multitwo) / div

            matrix[i][j] = frac
    
    print(matrix[numbs - 1][numbs - 1], "\n")
#2
def newton_method_and_approx():

    a = 7.2
    b = 7.4
    c = 7.5
    d = 7.6
    fa = 23.5492
    fb = 25.3913
    fc = 26.8224
    fd = 27.4589


    onedd = (fb - fa) / (b - a)
    twodd = (fc - fb) / (c - b)
    threedd = (fd - fc) / (d - c)
    ddone = (twodd - onedd) / (c - a)
    ddtwo = (threedd - twodd) / (d - b)
    ddonedd = (ddtwo - ddone) / (d - a)
    z = [onedd, ddone, ddonedd]
    print(z, "\n")
    #3
    aprox = 7.3
    approx = fa + onedd * (aprox - a) + ddone * (aprox - b) * (aprox - a)\
          + ddonedd * (aprox - c) * (aprox - b) * (aprox - a)
    print(approx, "\n")
#4
def function_name_here():

    one = 3.6
    two = 3.6
    three = 3.8
    four = 3.8
    five = 3.9
    six = 3.9
    oone = 1.675
    ttwo = 1.675
    tthree = 1.436
    ffour = 1.436
    ffive = 1.318
    ssix = 1.318
    oonee = 0
    ttwoo = -1.195
    tthreee = (tthree - ttwo) / (three - two)
    ffourr = -1.188
    ffivee = (ffive - ffour) / (five - four)
    ssixx = -1.182
    onee = 0
    twoo = 0
    threee = (tthreee - ttwoo) / (three - two)
    fourr = (ffourr - tthreee) / (four - two)
    fivee = (ffivee - ffourr) / (five - three)
    sixx = (ssixx - ffivee) / (six - four)
    oneone = 0
    twotwo = 0
    threethree = 0
    fourfour = (fourr - threee) / (four - one)
    fivefive = (fivee - fourr) / (five - two)
    sixsix = (sixx - fivee) / (six - three)
    ne = 0
    wo = 0
    hree = 0
    our = 0
    ive = (fivefive - fourfour) / (five - one)
    ix = (sixsix - fivefive) / (six - two)
    num = np.matrix([[one, oone, oonee, onee, oneone, ne], [two, ttwo, ttwoo, twoo, twotwo, wo], [three, tthree, tthreee, threee, threethree, hree], \
                   [four, ffour, ffourr, fourr, fourfour, our], [five, ffive, ffivee, fivee, fivefive, ive], [six, ssix, ssixx, sixx, sixsix, ix]])
    print(num, "\n")
#5      
def cubic_spline_matrix(x, y):

    size = len(x)
    matrix: np.array = np.zeros((size, size))
    matrix[0][0] = 1
    matrix[1][0] = x[1] - x[0]
    matrix[1][1] = 2 * ((x[1] - x[0]) + (x[2] - x[1]))
    matrix[1][2] = x[2] - x[1]
    matrix[2][1] = x[2] - x[1]
    matrix[2][2] = 2 * ((x[3] - x[2]) + (x[2] - x[1]))
    matrix[2][3] = x[3] - x[2]
    matrix[3][3] = 1
    print(matrix, "\n")

    q = 0
    r = ((3 / (x[2] - x[1])) * (y[2] - y[1])) - ((3 / (x[1] - x[0])) * (y[1] - y[0]))
    s = ((3 / (x[3] - x[2])) * (y[3] - y[2])) - ((3 / (x[2] - x[1])) * (y[2] - y[1]))
    t = 0
    u = np.array([q, r, s, t])
    print(u, "\n")

    m = [[matrix]]
    n = [[q], [r], [s], [t]]

    o = solve(m, n)

    print(o.T[0], "\n")


if __name__ == "__main__":
    np.set_printoptions(precision = 7, suppress = True, linewidth = 100)
    #1
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    approximated_x = 3.7 
    nevilles_method(x_points, y_points, approximated_x)
    #2,3
    newton_method_and_approx()
    #4
    function_name_here()
    #5
    x = [2, 5, 8, 10]
    y = [3, 5, 7, 9]
    cubic_spline_matrix(x, y)
