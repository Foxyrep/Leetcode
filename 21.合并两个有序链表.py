#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 双指针！纯自己写的
        c1, c2 = l1, l2
        # 当一个链表遍历完毕后，另一个直接堆在后面就可以
        ans = ListNode(0, None)
        ans_ = ans
        while c1 and c2:
            if c1.val <= c2.val:
                ans.next = c1
                ans = ans.next
                c1 = c1.next
                continue
            else: 
                ans.next = c2
                ans = ans.next
                c2 = c2.next
                continue

        ans.next = c1 if c1 else c2
        return ans_.next
        
# s = Solution()
# l1_3 = ListNode(4,None)
# l1_2 = ListNode(2,l1_3)
# l1_1 = ListNode(1,l1_2)
# l2_3 = ListNode(4,None)
# l2_2 = ListNode(3,l2_3)
# l2_1 = ListNode(1,l2_2)
# ans = s.mergeTwoLists(l1_1, l2_1)
# while ans:
#     print(ans.val)
#     ans = ans.next
        
# @lc code=end

