#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 栈！纯自己完成
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char == '}' and stack[-1] == '{': 
                stack.pop()
                continue
            if char == "]" and stack[-1] == '[':
                stack.pop()
                continue
            if char == ")" and stack[-1] == '(':
                stack.pop()
                continue
            stack.append(char)
        if not stack: return True
        return False
# @lc code=end

