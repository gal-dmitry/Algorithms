def main():
    # считываем элементы
    full_w, n = input().split()
    w = [int(i) for i in input().split()]

    # преобразуем тип
    w.insert(0, 0)
    full_w = int(full_w)
    n = int(n)

    # заводим массив D
    d = [[0 for j in range(full_w + 1)] for i in range(n + 1)]

    # проход по массиву
    for i in range(1, n + 1):
        for j in range(1, full_w + 1):
            d[i][j] = d[i - 1][j]
            if w[i] <= j:
                d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + w[i])

    # вывод
    print(d[n][full_w])


if __name__ == "__main__":
    main()