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
        
        num_1=''
        num_2=''
        
        while (l1!=None):
            num_1=num_1+str(l1.val)
            l1=l1.next
        
        
        
        while (l2!=None):
            num_2=num_2+str(l2.val)
            l2=l2.next
        
        
        num_1=num_1[::-1]
        num_2=num_2[::-1]
        
        print num_1
        print num_2
        
        sum0=int(num_1)+int(num_2)
        sum1=(str(sum0))[::-1]
        
        print sum1
        
        final1=ListNode(int(sum1[0]))
        list1=final1
                
        for j in range (1,len(sum1)):

            list1.next=ListNode(int(sum1[j]))
            list1=list1.next

        
        
        
        return (final1)