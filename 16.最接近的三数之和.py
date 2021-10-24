#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        # 自己的思路： 即找target-(a+b+c)最小
        # 仍然可以用15题的思路，三重循环，其中第二和第三种合并为双指针方法

        n = len(nums)
        nums.sort()
        ans = 0
        record = 999999999

        # 第一重循环
        for first in range(n):
            # 不能和刚刚遍历过的相等
            if first>0 and nums[first] == nums[first-1]:
                continue

            
            third = n-1
            # 第二重循环里两个指针逼近
            for second in range(first+1, n):
                # 同样的，不能和之前的相等
                if second>first+1 and nums[second] == nums[second-1]:
                    continue
                
                while second < third:
                    if abs(target-(nums[first]+nums[second]+nums[third])) < record:
                        ans = nums[first]+nums[second]+nums[third]
                    else: third -= 1
                
                if second == third:
                    break
                # 同步于mac
        return ans


            
# @lc code=end

