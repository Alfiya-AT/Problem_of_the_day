class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Str2LL(s):
    if not s:
        return None
    
    head = Node(s[0])
    curr = head
    
    for ch in s[1:]:
        curr.next = Node(ch)
        curr = curr.next
    
    return head


# 🔽 Call functions OUTSIDE class
head = Str2LL("Geeks")
res=""
# Print Linked List
temp = head
while temp:
    # print(temp.data, end=" -> ")
    # temp = temp.next

    res+=temp.data
    if temp.next:
        temp=temp.next.next
    else:
        break
print(res)
# print("NULL")