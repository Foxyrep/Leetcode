#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordslist = s.split(' ')
        for idx in range(len(wordslist)):
            idxrev = len(wordslist) - idx - 1
            if len(wordslist[idxrev]) > 0:
                return len(wordslist[idxrev])

# s = Solution()
# ss = "   fly me   to   the moon  "
# ans = s.lengthOfLastWord(ss)
# print(ans)

            
# @lc code=end

