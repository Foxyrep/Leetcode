#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbolList = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        ans = 0
        for (sym, n) in symbolList:
            while s.startswith(sym):
                ans += n
                s = s[len(sym):]
        return ans
# s = Solution()
# ans = s.romanToInt('MCMXCIV')
# print(ans)
# @lc code=end

