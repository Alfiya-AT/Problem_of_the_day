def total(arr,k):
    cnt=0
    for i in arr:
        # math formula for finding ceil
        cnt+=((i+k-1)//k)
    return cnt

k = 3
arr =[5, 8, 10, 13]
print(total(arr,k))