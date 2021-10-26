#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        l = None
        i = -1
        while True:
            i += 1
            if i == len(nums):
                break
            if not l:
                l = nums[i]
                continue
            if l != nums[i]:
                l = nums[i]
                continue
            if l == nums[i]:
                nums = nums[0:i]+nums[i+1:len(nums)]
                i -= 1
                continue
        return len(nums), nums

s = Solution()
ans, n = s.removeDuplicates([1,1,2])
print(ans)
print(n)

            
# @lc code=end

