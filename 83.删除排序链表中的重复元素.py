#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        递归条件：与基线条件相反
        基线条件：当头结点或者头结点的下一个结点是空的时候      
        操作：判断头结点值和下个节点值是是否相同，如果相同，则令头结点等于下个节点
        """
        if (head == None or head.next == None):
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head = head.next    
        return head



# @lc code=end

