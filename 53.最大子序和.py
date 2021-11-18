#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list) -> int:
        # 动态规划，用一个f(n)记录以第n个数结尾的所有子序列中和最大的
        # 那么f(n+1)=max{f(n),f(n)+nums[n+1]}
        # 按照这样的方法算所有的f(n)，里面最大的就是目标结果
        """
        动态规划最重要的思想就是**利用上一个状态**, 
        对于本题而言就是: **到底要不要加上上一个状态f(i-1)的信息**, 
        这完全取决于f(i-1)的**正负情况**, 
        这样我们就能得出了动态规划的递推公式: f(i)=max{f(i−1)+ai,ai}
        """

        f_n = [0]*len(nums)
        f_n[0] = nums[0]
        if len(nums) == 1: return nums[0]
        idx = 1
        while idx < len(nums):
            f_n[idx] = max(nums[idx], f_n[idx-1]+nums[idx])
            idx += 1
        return max(f_n)

# s = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# ans = s.maxSubArray(nums)
# print(ans)


# @lc code=end

