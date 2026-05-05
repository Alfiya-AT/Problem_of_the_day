#User function Template for python3
def find_minimum(a, b):
    # Your code here 
    # Return the minimum of all the valid operations
    min_val=a+b
    if min_val>a-b:
        min_val=a-b
    if min_val>a*b:
        min_val=a*b
    try:
        div=a/b
        if div<min_val:
            min_val=div
    except ZeroDivisionError :
        pass
    return min_val

print(find_minimum(5,0))