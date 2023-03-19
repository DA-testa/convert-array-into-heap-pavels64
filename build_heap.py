# python3


def keyboard():
    try:
        n = int(input().strip())
        if n <= 0:
            return None
        
        data = list(map(int, input().strip().split(" ")))
        return data
    
    except ValueError:
        return None



def file(name):
    try:
        with open(f"./tests/{name}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None
    except:
        return None
    
    n = contents[0].strip()
    if not n:
        return None
    
    data = list(map(int, contents[1].strip().split(" ")))
    if not data:
        return None
    
    return data


def sift_down(data, i, swaps):
    min = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < len(data) and data[left] < data[min]:
        min = left
        
    if right < len(data) and data[right] < data[min]:
        min = right
        
    if i == min:
        return
    
    swaps.append((i, min))
    data[i], data[min] = data[min], data[i]
    sift_down(data, min, swaps)


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
        name = input().strip()
        if str(name[-1]) != "a":
            data = file(name)
            if data:
                nulle, swaps = build_heap(data)
                print(nulle)
                
                for i, j in swaps:
                    print(i, j)
        else:
            print("Unable to build heap from file.")

if __name__ == "__main__":
    main()
