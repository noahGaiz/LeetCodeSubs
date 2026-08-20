# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        output = 0
        pointer = res
        carryover = 0
        while (l1 != None) or (l2 != None):  
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            output =  val1 + val2 + carryover
            if output < 10:
                res.val = output
                carryover = 0
                
            else: 
                output = output % 10
                res.val = output 
                carryover = 1
                
            
            if (l1 != None) or (l2 != None):
                res.next = ListNode()
                res = res.next
        if carryover == 1:
            res.next = ListNode()
            res = res.next
            res.val = 1
        return pointer