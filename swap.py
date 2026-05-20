def swap_ith(arr):
    i=0
    n=len(arr)
    while i+2<n:
        arr[i],arr[i+2]=arr[i+2],arr[i]
        i+=1
    return arr

arr=[1, 2, 3, 4, 5]
# arr= [1, 2, 3]
print(swap_ith(arr))