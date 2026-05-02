def duplicate(s):
    res=''
    for i in s:
        if i not in res:
            res+=i
    return res
s = "geEksforGEeks"
print(duplicate(s))
# Output: "geEksforG"