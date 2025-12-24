def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx]= arr[min_idx], arr[i]
arr=[19,8,12,9,5,7]
selection_sort(arr)
print("Sorted Array: ")
for i in range(len(arr)):
    print("%d, "%arr[i],end="")