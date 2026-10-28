def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr


n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

print("Sorted array:", insertion_sort(arr))
