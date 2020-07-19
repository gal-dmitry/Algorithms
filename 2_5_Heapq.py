import heapq


def main():
    h = []
    heapq.heapify(h)
    n = int(input())
    for _ in range(n):
        to_do = tuple(map(str, input().split()))

        if 'Insert' in to_do:
            number = -int(to_do[1])
            heapq.heappush(h, number)

        else:
            if h:
                max1 = heapq.heappop(h)
                print(-max1)


if __name__ == "__main__":
    main()
