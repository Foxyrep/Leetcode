#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list) -> list:
        """
        主要问题在于进位，从最后一位计算，定义一个进位的变量
        最后需要判定一下，最后的结果如果以0开头，或者最后carry = 1
        说明肯定原来是全9的数字，需要在开头再补一个1
        所以最后只需要前面加一个1就可以
        """
        carry = 0
        for idx in range(len(digits)):
            idxrev = len(digits) - 1 - idx
            sum = digits[idxrev] + carry
            if idx == 0:
                sum += 1
            digits[idxrev] = sum%10
            carry = sum//10
            if carry == 0:
                break
        if carry == 1: digits = [1] + digits
        return digits

# s = Solution()
# digits = [9,9]
# ans = s.plusOne(digits)
# print(ans)
            

# @lc code=end

