# python3


def build_heap(data):
    swaps = []
    n = len(data)
    # Perform heapify operation on every non-leaf node
    for i in range(n//2-1, -1, -1):
        min_heapify(data, i, n, swaps)
    return swaps

def min_heapify(data, i, n, swaps):
    # Find the indices of the left and right children
    left_child = 2*i + 1
    right_child = 2*i + 2
    # Find the index of the smallest node among the current node and its children
    smallest = i
    if left_child < n and data[left_child] < data[smallest]:
        smallest = left_child
    if right_child < n and data[right_child] < data[smallest]:
        smallest = right_child
    # If the smallest node is not the current node, swap them and continue heapifying
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        min_heapify(data, smallest, n, swaps)



def main():
    # Read input from user
    n = int(input().strip())
    data = list(map(int, input().strip().split()))

    # Check input constraints
    assert n == len(data)

    # Call build_heap to get swap operations
    swaps = build_heap(data)

    # Check output constraints
    assert len(swaps) <= 4 * n

    # Print number of swaps and swap operations
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
