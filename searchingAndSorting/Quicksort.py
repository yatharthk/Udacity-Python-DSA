"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while pivot >= arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    else:
        arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
    return arr


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test) - 1))

# Method2
# def quicksort(array):
#     n=len(array)

#     if n<2:
#         return array

#     current=0
#     pivot=array[0]
#     for i in range(1,n):
#         if pivot>=array[i]:
#             current+=1
#             array[i],array[current]=array[current],array[i]
#     array[0],array[current]=array[current],array[0]

#     left=quicksort(array[0:current])
#     right=quicksort(array[current+1:n])
#     return left+[array[current]]+right
