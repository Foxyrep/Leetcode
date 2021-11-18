#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        牛顿迭代法
        """
        r = x
        while r*r > x:
            r = int((r + x/r)/2)
        return r
        
# @lc code=end


