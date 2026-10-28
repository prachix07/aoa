def partition(arr, low, high):
    pivot = arr[low]
    start = low + 1
    end = high

    while True:
        while start <= end and arr[start] <= pivot:
            start += 1

        while start <= end and arr[end] > pivot:
            end -= 1

        if start > end:
            break

        arr[start], arr[end] = arr[end], arr[start]

    arr[low], arr[end] = arr[end], arr[low]
    return end


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)
