# easy problem
# skills learn: 2 pointers, now what correct value to return, check if all values get updated
# Runtime: O(n + m)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = ListNode(-1)
        current_node = prev
        
        #device where prev is pointing
        while l1 and l2:
            #comparing part
            if l1.val <= l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
                
        #out of the loop means either n1 or n2 is at the end
        if l1:
            current_node.next = l1
        if l2:
            current_node.next = l2
            
        # initially returned current_node.next, but I forgot current_node was being updated and now at the end
        return prev.next
  
