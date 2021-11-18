#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        先把短的串前补0至和长串同长度
        最后还是要判断一下，都结束后carry为1，说明前面还有一位进位需要加到开头
        """

        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        if len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b

        carry = 0
        ansstr = ''
        for idx in range(len(a)):
            idxrev = len(a) - 1 - idx
            sum = int(a[idxrev]) + int(b[idxrev]) + carry
            cur = sum%2
            ansstr = str(cur) + ansstr
            carry = sum//2
        if carry == 1: ansstr = '1' + ansstr
        return ansstr

# s = Solution()
# ans = s.addBinary('0', '0')
# print(ans)


# @lc code=end

