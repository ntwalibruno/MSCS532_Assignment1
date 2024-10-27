def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

array = [50,560,100,40,20]

print("Original array: ", array)

sort(array)

print("Sorted array  : ", array)