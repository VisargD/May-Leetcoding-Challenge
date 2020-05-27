# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # Check if the linked list is empty.
        if head == None:
            return None
        
        # Initialize a pointer to head.
        head1 = head

        # Initialize two more pointers to the element after head.
        head2 = head3 = head1.next
        
        # Check if next two nodes are null or not.
        # If not null then move into the while loop.
        while head2 != None and head2.next != None:
            
            # Linking odd and even nodes together.
            head1.next = head2.next            
            head1 = head1.next           
            head2.next = head1.next           
            head2 = head2.next
            
        # After loop, all the odd nodes will be together in the beginning. 
        # So link the first even node (head3) to the last odd node (head1)
        head1.next = head3
        return head
