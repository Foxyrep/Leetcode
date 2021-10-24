#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # 指针对撞法，每次把高度较小的那个边的索引向内加一
    # 逻辑是：
    # 
    def maxArea(self, height) -> int:
        def calArea(self, index_l, index_r):
            return min(height[index_l],height[index_r])*(index_r-index_l)
        index_l, index_r = 0, len(height)-1
        record = 0
        while index_l<index_r:
                area = calArea(self, index_l, index_r) 
                record  = max(record, area)
                if height[index_l] <= height[index_r]:
                    index_l += 1
                else: index_r -= 1
        return record
    
    
# @lc code=end

