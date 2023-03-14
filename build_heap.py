# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while 2 * j + 1 < n:
            k = 2 * j + 1
            if k + 1 < n and data[k + 1] < data[k]:
                k += 1
            if data[j] > data[k]:
                data[j], data[k] = data[k], data[j]
                swaps.append((j, k))
                j = k
            else:
                break
    return swaps


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
