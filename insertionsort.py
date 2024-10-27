#Insertion sort funtion - will sort array in in monotonically decreasing order
def sort(arr):
    #loop through the entire array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        #compare current key(item) to preceding item
        #if item is less than key(item) it will be moved to the key's current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

array = [50,560,100,40,20,100]

#print original array
print("Original array: ", array)

sort(array)

#print sorted array
print("Sorted array  : ", array)