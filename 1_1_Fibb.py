def main():
    n = int(input())
    m = [0, 1]
    while n > 1:
        a = m[0] + m[1]
        m[0] = m[1]
        m[1] = a
        n -= 1
    print(m[1])

if __name__ == "__main__":
    main()