# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        root = ListNode(l1.val + l2.val)
        pointer1 = l1.next
        pointer2 = l2.next
        pointer = root
        
        while pointer1 != None and pointer2 != None:
            pointer.next = ListNode(pointer1.val + pointer2.val)
            pointer = pointer.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        if pointer1 == None and pointer2 != None:
            pointer.next = pointer2
        if pointer2 == None and pointer1 != None:
            pointer.next = pointer1
            
        pointer = root
        while pointer != None:
            if pointer.val >= 10:
                if pointer.next == None:
                    pointer.next = ListNode(pointer.val // 10)
                else:
                    pointer.next.val += pointer.val // 10
                pointer.val = pointer.val % 10
            pointer = pointer.next
        return root
