#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start


class Solution:
    def fourSum(self, nums, target: int):
        # 先按照三数之和的双指针法思路尝试：
        nums.sort()
        n = len(nums)
        ans = []
        for first in range(n):
            if first>0 and nums[first] == nums[first-1]:
                continue

            for second in range(first+1, n):
                if second>first+1 and nums[second] == nums[second-1]:
                    continue

                third = second+1 
                forth = n-1
                while third < forth:
                    sum = nums[first] + nums[second] + nums[third] + nums[forth]
                    if sum == target:
                        ans.append([nums[first],nums[second],nums[third],nums[forth]])
                        while third<forth and nums[third] == nums[third+1]:
                            third += 1
                        third += 1
                        while third<forth and nums[forth] == nums[forth-1]:
                            forth -= 1
                        forth -= 1
                        
                    if sum > target:
                        forth -= 1

                    elif sum < target:
                        third += 1
                    
        return ans

# s = Solution()
# ans = s.fourSum(nums=[2,2,2,2,2], target=8)
# print(ans)
#           需要注意一个问题
#   最接近的几数之和 和 几数之和 各重循环里判定与前一次不相等的目的是不同的
#   前者是因为每次都得比较，所以快速跳过肯定相同的，节省时间
#   后者是为了避免输出重复解，去重
# 
# 
#       
# @lc code=end

