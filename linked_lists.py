# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode(0) # points to head node
        current = merged_list # points to current node 
        # When you use current = merged_list, current and merged_list 
        # are both references to the same object in memory. 
        # This means that if you update the object through one of the references, 
        # the other reference will reflect the change.


        list1_ptr = list1
        list2_ptr = list2

        while list1_ptr != None or list2_ptr != None:
            if list1_ptr == None:
                current.next = ListNode(list2_ptr.val)
                current = current.next
                list2_ptr = list2_ptr.next

            elif list2_ptr == None:
                current.next = ListNode(list1_ptr.val)
                current = current.next
                list1_ptr = list1_ptr.next  

            else:
                if list1_ptr.val < list2_ptr.val:
                    current.next = ListNode(list1_ptr.val)
                    current = current.next
                    list1_ptr = list1_ptr.next
                else:
                    current.next = ListNode(list2_ptr.val)
                    current = current.next
                    list2_ptr = list2_ptr.next
      

        return merged_list.next
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers: prev as None, current as head and next as None
        prev_val = None
        current_val = head
        next_val = None
        
        # Traverse through the list
        while current_val != None:
            # Store next node
            next_val = current_val.next
            # reverse current node's pointer
            current_val.next = prev_val
            # move prev and current one step forward
            prev_val = current_val
            current_val = next_val
        
        # return the reversed list
        return prev_val
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        h = head
        # Count the number of nodes in the list
        while h:
            length += 1
            h = h.next
        middle = (length + 1) // 2 if length % 2 == 1 else (length // 2) + 1
        c = 0
        h = head
        while h:
            c += 1
            if c == middle:
                return h
            h = h.next

