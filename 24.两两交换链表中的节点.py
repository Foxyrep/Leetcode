#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 可以用递归的方法，但是实际上递归消耗更多内存
        # 因此直接用迭代（遍历）的方式就好，反正时间复杂度都是n

        # 如果节点数为0或1，直接返回原链表
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        p = dummy
        # 开始时交换前两个,交换完后再把node1付给p，这样p.next就是下一对的第一个节点了
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            p.next = node2
            node1.next = node2.next
            node2.next = node1
            p = node1
        return dummy.next



# @lc code=end

