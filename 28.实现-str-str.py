#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 双指针法？下面这种方法逻辑可行但是明显n2的复杂度，超时了
        # 经典的KMP算法！
        if not needle: return 0

        m = len(haystack)
        n = len(needle)
        if m<n: return -1

        # 首先要获得子串的next值
        slow = fast = 0
        while slow<m:
            if haystack[slow] == needle[fast]:
                fast += 1
                slow += 1
                if fast == n:
                    return slow-n
            else:
                if fast>0:
                    slow = slow-fast+1
                    fast = 0
                else: slow += 1
        return -1

# s = Solution()
# ans = s.strStr(haystack = "mississippi", needle = "issip")
# print(ans)

    
# @lc code=end

