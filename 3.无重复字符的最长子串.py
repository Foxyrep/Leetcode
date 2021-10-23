#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
import typing


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        record = 1
        # dic = dict() 不用字典，用集合，只需要记录有没有出现过，不需要记录位置
        occ = set()
        left = 0
        right = -1
        while left<len(s):
            if left != 0:
                occ.remove(s[left-1])
            while right+1<len(s) and s[right+1] not in occ:
                occ.add(s[right+1])
                right += 1
            record = max(record, right-left+1)
            left += 1
        return record

# # 调试用
# s = Solution()
# res = s.lengthOfLongestSubstring("dvdf")
# print(res)

# @lc code=end

