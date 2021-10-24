#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力解法肯定是遍历 N^2 次，pass, 注意nums并不是递增的
        # 思路：
        # 遍历数组，把每个元素及其下标存入字典
        # 因为在字典里搜索时间复杂度永远是o(1)，所以总复杂度为o(n)
        dic = dict()
        for i in range(len(nums)):
            # 判断如果字典里存了能和nums[i]组成target的，就直接输出下标
            if target - nums[i] in dic.keys():
                return [i, dic[target-nums[i]]]
            else:
                dic[nums[i]] = i
                


# @lc code=end

