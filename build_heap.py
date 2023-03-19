# python3


def keyboard():
    try:
        n = int(input().strip())
        if n <= 0:
            return None
        
        data = list(map(int, input().strip().split(" ")))
        return data
    
    except ValueError:
        print("Invalid input: n must be a positive integer")
        return None



def file(filename):
    try:
        with open(f"./tests/{filename}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None
    except:
        print("Error reading file")
        return None
    
    n = contents[0].strip()
    if not n:
        print("Invalid input: n not provided")
        return None
    
    data = list(map(int, contents[1].strip().split(" ")))
    if not data:
        print("Invalid input: data not provided")
        return None
    
    return data


def sift_down(data, i, swaps):
    min_index = i
    
    left = 2 * i + 1
    if left < len(data):
        _, min_index = min(enumerate([data[left], data[min_index]]), key=lambda x: x[1])
        if min_index != i:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(data, min_index, swaps)
    
    right = 2 * i + 2
    if right < len(data):
        _, min_index = min(enumerate([data[right], data[min_index]]), key=lambda x: x[1])
        if min_index != i:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(data, min_index, swaps)


def build_heap(data):
    swaps = []
    nulle = 0
    i = len(data) // 2
    while i >= 0:
        sift_down(data, i, swaps)
        nulle = max(nulle, len(swaps))
        i -= 1
    return nulle, swaps



def main():
    input_method = input().strip()

    if input_method == "I":
        data = keyboard()
        if data:
            nulle, swaps = build_heap(data)
            print(nulle)

            for i, j in swaps:
                print(i, j)

    elif input_method == "F":
        filename = input().strip()
        if str(filename[-1]) != "a":
            data = file(filename)
            if data:
                nulle, swaps = build_heap(data)
                print(nulle)
                
                for i, j in swaps:
                    print(i, j)
        else:
            print("Unable to build heap from file.")

if __name__ == "__main__":
    main()
