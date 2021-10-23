#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 本题用python3写和用java，c++有很大不同！
        # 因为python负数取余和取整规则不同
        # x的正负必须分开讨论
        import math
        ans = 0
        while x!=0:
            if x>0:  
                ans = ans*10 + x%(10)
                x = x//10
            else: 
                ans = ans*10 + x%(-10)  #  负数对正数取余得到欠余数，是不对的，必须改成对负数取余，才能得到负数
                x = math.ceil(x/10)     #  负数取整是向下取整，这里必须用ceil强行向上取整
        if ans<-2**31 or ans>2**31-1:
            return 0
        return ans 

# s = Solution()
# ans = s.reverse(-123)
# print(ans)

# @lc code=end

