from bisect import bisect_right

def CountElements(a, b, n, query, q):

    result = []

    b.sort()

    for i in query:

        cnt = bisect_right(b, a[i])

        result.append(cnt)

    return result


n = 3

a = [4,1,2]

b = [1,7,3]

query = [0,1]

q = 2

print(CountElements(a,b,n,query,q))