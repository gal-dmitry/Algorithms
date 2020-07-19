import heapq
import sys


def fractional_knapsack(capacity, values_and_weights):
    h = []
    for value, weight in values_and_weights:
        top = -value / weight
        element = (top, weight, value)
        h.append(element)
    heapq.heapify(h)

    acc = 0
    while h and capacity:
        el = heapq.heappop(h)
        if capacity - el[1] >= 0:
            capacity -= el[1]
            acc += el[2]
        else:
            acc += -el[0] * capacity
            break
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))


if __name__ == '__main__':
    main()