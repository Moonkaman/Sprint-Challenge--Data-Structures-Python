def merge(arrA, arrB):
    merged_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
        smallest = min(arrA[0], arrB[0])
        if smallest == arrA[0]:
            arrA.pop(0)
        else:
            arrB.pop(0)

        merged_arr.append(smallest)

    if len(arrA) > 0:
        for num in arrA:
            merged_arr.append(num)
    else:
        for num in arrB:
            merged_arr.append(num)
    return merged_arr


def merge_sort(arr):
    if(len(arr) > 1):
        left = merge_sort(arr[0:int(len(arr)/2)])
        right = merge_sort(arr[int(len(arr)/2):])
        arr = merge(left, right)

    return arr
