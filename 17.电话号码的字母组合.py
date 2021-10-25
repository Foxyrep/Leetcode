#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str):
        # # 热评第一的答案：思路就是分层遍历
        # Table = [
        #     ['a', 'b', 'c'],
        #     ['d', 'e', 'f'],
        #     ['g', 'h', 'i'],
        #     ['j', 'k', 'l'],
        #     ['m', 'n', 'o'],
        #     ['p', 'q', 'r', 's'],
        #     ['t', 'u', 'v'],
        #     ['w', 'x', 'y', 'z'],
        #     ]
        # if digits == '':
        #     return []
        # ans = ['']
        # for num in digits:
        #     ans = [pre+cur for pre in ans for cur in Table[int(num)-2]]
        # return ans

        # 官方题解：回溯法,一般看到穷举的题目，都要想到回溯法：
        # Time Beats还没有第一种方法高
        if not digits: return []
        # 先定义一个哈希表
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index: int):

            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


# s = Solution()
# ans = s.letterCombinations("234")
# print(ans)



# @lc code=end

