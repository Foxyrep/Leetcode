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
        ans = 999999999

        # 第一重循环
        for first in range(n):
            # 不能和刚刚遍历过的相等
            if first>0 and nums[first] == nums[first-1]:
                continue

            second = first+1
            third = n-1
            # 第二重循环里两个指针逼近
            while second < third:
                sum = nums[first]+nums[second]+nums[third]
                # 如果直接相等，可以直接返回：
                if sum == target:
                    return sum

                if abs(sum-target) < abs(ans-target):
                    ans = sum
                
                if sum > target:
                    third_ = third - 1  # 这里得暂存一下，然后比较一下，得找到下一个不相等的才能赋值
                    while third_ > second and nums[third_] == nums[third]:
                        third_ -= 1
                    third = third_
                elif sum < target:
                    second_ = second + 1
                    while second_ < third and nums[second_] == nums[second]:
                        second_ += 1 
                    second = second_

                # 同步于mac
        return ans

# s = Solution()
# ans = s.threeSumClosest([0,0,0,3,2,1],7)
# print(ans)
            
# @lc code=end

