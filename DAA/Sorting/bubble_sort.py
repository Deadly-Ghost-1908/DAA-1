def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped = True
        if(swapped==False):
            break
arr=[19,8,12,9,5,7]
bubble_sort(arr)
print("Sorted Array: ")
for i in range(len(arr)):
    print("%d, "%arr[i],end="")
    
   