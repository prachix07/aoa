def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

print("Sorted array:", selection_sort(arr))
