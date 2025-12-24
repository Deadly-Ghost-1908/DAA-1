import random
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + mid + randomized_quicksort(right)
arr = [9, 4, 7, 3, 1, 8]
print("Sorted:", randomized_quicksort(arr))




