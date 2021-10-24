#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 和第7题结合，先反转，再判定是否和原来的数相等
        # 可以直接排除所有负数
        if x<0 or (x%10==0 and x!=0): return False
        if x == 0: return True

        else:
            # def reverse(self, x: int) -> int:
            #     # 本题用python3写和用java，c++有很大不同！
            #     # 因为python负数取余和取整规则不同
            #     # x的正负必须分开讨论
            #     import math
            #     ans = 0
            #     while x!=0:
            #             ans = ans*10 + x%(10)
            #             x = x//10
            #     if ans<-2**31 or ans>2**31-1:
            #         return 0
            #     return ans 
            # if reverse(self,x)==x: return True

            # 但是还可以优化！
            # 可以只翻转前半部分，并与原来数的后半部分比较，如果相等，则是回文数
            # 如何知道已经反转了一般的数字？
            # 可以想到，如果在某一步，反转后的数字已经大于源数字的时候，就已经转了一半
            def reverse_half(self, x: int) -> int:
                import math
                ans = 0
                while x>ans:
                        ans = ans*10 + x%(10)
                        x = x//10
                return x, ans 
            x, ans = reverse_half(self,x)
            if x==ans or x==ans//10: return True
        return False

# s = Solution()
# ans = s.isPalindrome(121)
# print(ans)
# @lc code=end

