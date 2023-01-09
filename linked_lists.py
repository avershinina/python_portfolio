# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# To combine the lists, you can create a new list and add the names from both of the original lists to it. 
# You can do this by creating a new node for each name and linking it to the end of the new list.
# To keep track of the new list, you can use a pointer called current that points to the current position in the list. 
# You can also use another pointer called merged_list that points to the head of the list (the first node).

# # Set up an empty merged list
# merged_list = null

# # Set up a pointer to the head of the merged list
# current = merged_list

# # Set up pointers to the heads of the input lists
# list1_ptr = head of list1
# list2_ptr = head of list2

# # Loop until both pointers are null
# while list1_ptr is not null or list2_ptr is not null:
#     # Check if list1_ptr is not null
#     if list1_ptr is not null:
#         # Add the current node from list1 to the merged list
#         current.next = ListNode(list1_ptr.val)
#         current = current.next
#         list1_ptr = list1_ptr.next

#     # Check if list2_ptr is not null
#     if list2_ptr is not null:
#         # Add the current node from list2 to the merged list
#         current.next = ListNode(list2_ptr.val)
#         current = current.next
#         list2_ptr = list2_ptr.next

# # Return the head of the merged list
# return merged_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode(0) # points to head node

        print("Merged", merged_list)
        current = merged_list # points to current node 
        # When you use current = merged_list, current and merged_list 
        # are both references to the same object in memory. 
        # This means that if you update the object through one of the references, 
        # the other reference will reflect the change.


        list1_ptr = list1
        list2_ptr = list2

        while list1_ptr != None or list2_ptr != None:
            if list1_ptr != None:
                current.next = ListNode(list1_ptr.val)
                current = current.next
                list1_ptr = list1_ptr.next
                print("Merged", merged_list)

            if list2_ptr != None:
                current.next = ListNode(list2_ptr.val)
                current = current.next
                list2_ptr = list2_ptr.next
                print("Merged", merged_list)
        

        return merged_list.next
