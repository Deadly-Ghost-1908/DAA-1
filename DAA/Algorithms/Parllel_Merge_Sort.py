from multiprocessing import Pool
def merge(a,b):
    r=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]: r.append(a[i]); i+=1
        else: r.append(b[j]); j+=1
    return r+a[i:]+b[j:]
def pmergesort(arr):
    if len(arr)<=1: return arr
    mid=len(arr)//2
    if len(arr)<10000: return merge(pmergesort(arr[:mid]), pmergesort(arr[mid:]))
    with Pool(2) as p:
        left,right = p.map(pmergesort, (arr[:mid], arr[mid:]))
    return merge(left,right)
if __name__=="__main__":
    import random
    a=[random.randint(0,100) for _ in range(20)]
    print("in:",a)
    print("out:", pmergesort(a))



