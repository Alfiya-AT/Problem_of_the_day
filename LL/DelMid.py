class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMid(self, head):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head

def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")

# 🔽 Create Linked List
head = Node(5)
head.next = Node(4)
head.next.next = Node(8)

# 🔽 Call function
obj = Solution()
new_head = obj.deleteMid(head)

# 🔽 Print result
printLL(new_head)