#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import NewType


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def get_K_th(k):
            # 要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            # 这两个index是来指示当前数组的开头从哪里开始。（删除元素后，开头不再是0处）
            index1, index2 = 0, 0
            while True:
                # 如果nums1的指针越界，就返回nums2的第k小元素,反之亦然；如果k==1，直接返回两个数组开头更小的那个
                if index1 == m:  
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                #
                index1_new = min(index1+k//2-1, m-1) # 防止越界
                index2_new = min(index2+k//2-1, n-1) # 防止越界
                pivot1, pivot2 = nums1[index1_new], nums2[index2_new] 
                if pivot1 <= pivot2:
                    k -= index1_new - index1 + 1 # 因为如果越界，那么去除的就不一定是k//2，因此不能简单的写成k//2
                    index1 = index1_new + 1
                else: 
                    k -= index2_new -index2 + 1
                    index2 = index2_new + 1
        # 定义k
        m, n = len(nums1), len(nums2)
        if (m+n)%2 == 1:
            k = (m+n+1)//2 
            return get_K_th(k)
        else:
            mid1, mid2 = (m+n)//2, (m+n)//2+1
            k1,k2 = mid1, mid2
            return (get_K_th(k1)+get_K_th(k2))/2

s = Solution()
ans = s.findMedianSortedArrays([1,2,3,4],[5,6,7,8,9])
print(ans)
# @lc code=end

