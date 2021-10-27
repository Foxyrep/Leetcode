#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        if not nums:
            return 0
        slow = fast = 0 
        n = len(nums)
        while fast<n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 
            fast += 1
        return slow

# s = Solution()
# ans = s.removeElement([1,1,2,2,4,2,3,2,5], 2)
# print(ans)


# @lc code=end

