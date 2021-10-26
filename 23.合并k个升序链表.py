#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from heapq import heappop, heappush


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # 维护一个按顺序排列的list，元祖排序会默认按照第一个元素排序
        # 这个按顺序排列的list，用优先队列！
        # 并且给ListNode重写比较函数，使其可以比较
        
        def __lt__(self,other):
            return self.val < other.val
        ListNode.__lt__ = __lt__

        dummy = ListNode(0, None)
        p = dummy
        heap = []

        for l in lists:
            if l:
                heappush(heap, l)
        while heap:
            node = heappop(heap)
            p.next = ListNode(node.val, None)
            p = p.next
            if node.next: heappush(heap, node.next)
        return dummy.next

# s = Solution()
# l1_3 = ListNode(4,None)
# l1_2 = ListNode(2,l1_3)
# l1_1 = ListNode(1,l1_2)
# l2_3 = ListNode(4,None)
# l2_2 = ListNode(3,l2_3)
# l2_1 = ListNode(2,l2_2)
# ans = s.mergeKLists([l1_1, l2_1])
# while ans:
#     print(ans.val)
#     ans = ans.next

# @lc code=end

