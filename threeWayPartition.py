def partitioning(arr,a,b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:

        # Elements smaller than a
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        # Elements between a and b
        elif a <= arr[mid] <= b:
            mid += 1

        # Elements greater than b
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

    # val_b=0
    # left=len(arr)-1
    # val_a=0
    # val_ab=0
    # while left>-1:
    #     if arr[left]>b and val_b==0:
    #         left-=1
    #     elif arr[left]<=b and arr[left]>=a and val_ab==0:
    #         val_b=1
    #         left-=1
    #     elif arr[left]<a and val_a==0:
    #         val_ab=1
    #         left-=1
    #     else:
    #         return False
    # return True

print(partitioning(arr=[1, 2, 3, 3, 4],a=1,b=2))