import random
import numpy as np


def one(matrix):
    print("one")
    print(round(np.linalg.det(matrix),3))
    print()


def two(matrix):
    print("two")
    print(np.array(matrix).swapaxes(0, 1))
    print()


def three(matrix, n):
    print("three")
    a = np.array(matrix)
    for i in range(n):
        print(a[a[:, i].argsort()])
    print()


def four(matrix, n):
    print("four")
    m = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            m.append(matrix[i][j])
    m.sort()
    for i in range(len(m)):
        if (i % n == 0 and i != 0):
            print("\n" + str(m[i]), end=" ")
        else:
            print(m[i], end=" ")
    print("\n")
    m.reverse()
    for i in range(len(m)):
        if (i % n == 0 and i != 0):
            print("\n" + str(m[i]), end=" ")
        else:
            print(m[i], end=" ")
    print("\n")


def five(matrix):
    print("five")
    m = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            m.append(matrix[i][j])
    a = max(m)
    b = min(m)
    print("before " + str(m))
    for i in range(len(m)):
        if (m[i] == a):
            m[i] = b
        elif (m[i] == b):
            m[i] = a
    print("max = " + str(a))
    print("min = " + str(b))
    print("after " + str(m) + "\n")


def six(matrix):
    print("six*")
    print(np.array(tuple(zip(*sorted(zip(*matrix), key=sum)))))
    print()


def seven(matrix):
    print("seven")
    print(np.linalg.matrix_power(matrix, 2))
    print()
    print(np.linalg.matrix_power(matrix, 3))
    print()
    print(np.linalg.matrix_power(matrix, 4))
    print()


def eigth(matrix):
    print("eight")
    print(np.linalg.inv(matrix))
    print()


def main():
    n = int(input("Enter size of matrix: "))

    matrix = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(0, 10)

    print(matrix)

    one(matrix)
    two(matrix)
    three(matrix, n)
    four(matrix, n)
    five(matrix)
    six(matrix)
    seven(matrix)
    eigth(matrix)


if __name__ == "__main__":
    main()
