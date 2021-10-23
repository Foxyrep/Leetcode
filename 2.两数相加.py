#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# # 用于调试，提交时要注释掉
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 需要注意进位问题
        res = curr = ListNode()
        carry = 0 # 进位值
        while carry or l1 or l2:
            val = carry  # val每次循环开始都是0，所以一开始赋值carry相当于加上carry
            if l1:
                val = l1.val + val  # 
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            carry, val = divmod(val, 10)  # 分别是商和余数
            curr.next = ListNode(val)
            curr = curr.next
        return res.next


# # 用于调试，提交时要注释掉
# l2_4 = ListNode(4)
# l1_3 = ListNode(3)
# l2_3 = ListNode(4,l2_4)
# l1_2 = ListNode(4,l1_3)
# l2_2 = ListNode(6,l2_3)
# l1 = ListNode(2,l1_2)
# l2 = ListNode(5,l2_2)

# S = Solution()
# res = S.addTwoNumbers(l1,l2)
# print(res)


# @lc code=end

