#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 问题在于一开始不知道链表有多长，所以常规方法必须循环两次，第一次知道多长
        # 第二次再去掉正数第 sz-n+1 个节点
        # 如何用一次循环解决？
        # 双指针法：
        # 初始化left=0, right=0+n,同时移动，当right到末节点时，left就指向倒数第n个节点
        
        ans = ListNode(0,head)
        left = ans
        right = head
        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return ans.next

# s = Solution()            
# head_5 = ListNode(5,None)
# head_4 = ListNode(4,head_5)
# head_3 = ListNode(3,head_4)
# head_2 = ListNode(2,head_3)
# head = ListNode(1,head_2)
# # head = ListNode(1,None)

# ans = s.removeNthFromEnd(head, 1)
# while ans:
#     print(ans.val)
#     ans = ans.next
        
# @lc code=end

