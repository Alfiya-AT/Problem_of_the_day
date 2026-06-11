from collections import Counter
def longestPalindrome(s):
    count=0
    count=Counter(s)
    oddCount=0
    lenOfPalindrome=0
    for key, value in count.items():
        if value%2==0:
            lenOfPalindrome+=value
        else:
            lenOfPalindrome+=(value-1)
            oddCount+=1
    if oddCount > 0:
        lenOfPalindrome+=1
    return lenOfPalindrome

s = "abccccdd"
print(longestPalindrome(s))