def partitioning(arr,a,b):
    left=0
    d={}
    for i in arr:
        if i<a:
            d['low']=d.get(d['low'],0)+1
        elif i>=a and i<=b:
            d['mid']=d.get(d['mid'],0)+1
        else:
            d['high']=d.get(d['high'],0)+1
    l=0
    m=d['mid']
    while arr[i]<a:

    


    
    return arr

print(partitioning(arr=[1, 2, 3, 3, 4],a=1,b=2))