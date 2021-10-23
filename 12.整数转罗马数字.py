#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # 根据罗马数字的唯一表示法，为了表示一个给定的整数 \textit{num}num，我们寻找不超过 \textit{num}num 的最大符号值，将 \textit{num}num 减去该符号值，然后继续寻找不超过 \textit{num}num 的最大符号值，将该符号拼接在上一个找到的符号之后，循环直至 \textit{num}num 为 00。最后得到的字符串即为 \textit{num}num 的罗马数字表示。
        # 编程时，可以建立一个数值-符号对的列表 \textit{valueSymbols}valueSymbols，按数值从大到小排列。遍历 \textit{valueSymbols}valueSymbols 中的每个数值-符号对，若当前数值 \textit{value}value 不超过 \textit{num}num，则从 \textit{num}num 中不断减去 \textit{value}value，直至 \textit{num}num 小于 \textit{value}value，然后遍历下一个数值-符号对。若遍历中 \textit{num}num 为 00 则跳出循环
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
        s = ''
        for (sym, n) in symbolList:
            while n<=num: 
                num = num - n
                s = s + sym
        return s

s = Solution()
ans = s.intToRoman(1994)
print(ans)
# @lc code=end

