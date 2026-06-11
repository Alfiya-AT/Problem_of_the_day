def findWords():
    words = ["Hello", "Alaska", "Dad", "Peace"]
    row = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    res=[]

    for i in words:
        ch=0
        flag1=True
        while ch<len(i):
            j=0
            flag = False
            while j<len(row):
                # print(ch)
                if i[ch] in row[j]:
                    flag=True
                    break
                j+=1
            if flag==True:
                break
            else:
                flag1=False
            ch+=1
        if flag1==True:
            res.append(i)
    return res

print(findWords())