#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


from math import tanh
from typing import TYPE_CHECKING, runtime_checkable


class Solution:
    def threeSum(self, nums):
        # 遍历元素，对每个元素用两数之和的方法求三个数和为0的情况,N2复杂度
        # 对最后的结果去重，去重的方法是对结果中每个列表排序
        # 这种方法事件复杂度应该是N2，但是却通不过全是0的例子
        # 这种方法需要哈希去重，占用的空间比较高，算是不正确的答案
        # def sum2(self, pos, nums, target):
        #     dic = dict()
        #     ansList = []
        #     for i in range(len(nums)):
        #         # 判断如果字典里存了能和nums[i]组成target的，
        #         if target - nums[i] in dic.keys():
        #             ansList.append([pos, nums[i], target-nums[i]])
        #         else:
        #             dic[nums[i]] = i
        #     # ansList = list(set(ansList))
        #     return ansList

        # ans = []
        # for i in range(len(nums)):
        #     target = 0 - nums[i]
        #     nums_ = nums[0:i]+nums[i+1:len(nums)]
        #     anslist = sum2(self, nums[i], nums_, target)
        #     ans = ans +anslist

        # #  去重
        # for i in range(len(ans)):
        #     ans[i].sort()
        #     ans[i] = tuple(ans[i])
        # ans = list(set(ans))
        # for i in range(len(ans)):
        #     ans[i] = list(ans[i])
        
        # return ans


        # 下面使用题解的思路，先排序，再遍历元素，对每次遍历中使用双指针
        n = len(nums)
        ans = []
        nums.sort()

        # 遍历排序后的数组，这是第一重循环
        for first in range(n):
            # 必须和遍历的上一个不同，因为如果相同，则最后得到的肯定是相同的解集合
            # 因此下面判定如果相同，就跳过本次循环
            if first>0 and nums[first] == nums[first-1]:
                continue

            second = first+1
            third = n-1
            # 第二重循环，second和third是双指针，同时从两端向中间移动
            # for second in range(first+1,n):
            #     # 同样的，也必须和遍历的上一个结果不同，否则没有意义，肯定是重复的
            #     if second>first+1 and nums[second] == nums[second-1]:
            #         continue
            #     # 循环的条件是second在third左侧
            #     # 如果second，third加起来大于target，则左移third，直到两者重合
            #     while second < third and nums[second] + nums[third] > target:
            #         third -= 1
            #     # 如果重合了，之后再左移third也不会有了，因为这种情况已经在之前的second遍历中遇到过了
            #     if second == third:
            #         break
            #     if nums[second] +nums[third] == target:
            #         ans.append([nums[first], nums[second], nums[third]])
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    ans.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    third -= 1

                elif sum<0:
                    second += 1
                elif sum>0:
                    third -= 1

        return ans


        
# s = Solution()
# s.threeSum(nums=[0])
# @lc code=end

