#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
import typing


class Solution:
    def generateParenthesis(self, n: int) -> list:
        # 看到生成所有可能性，首先想到尝试用回溯法：
        ans_set = []
        ans = []

        def backtrack(ans, left, right):
            if len(ans) == n*2:
                ans_set.append("".join(ans))
                # return
            if left<n:   # 如果左括号少于三个，这个是关键逻辑！
                ans.append('(')
                backtrack(ans,left+1,right)
                ans.pop()
            if right<left: # 如果又括号比左括号少，这个是关键逻辑！
                ans.append(')')
                backtrack(ans,left, right+1)
                ans.pop()

        # left right分别指示当前序列中左右括号的个数
        backtrack(ans,0,0)
        return ans_set

s = Solution()   
ans = s.generateParenthesis(3)
print(ans)
        
# @lc code=end

