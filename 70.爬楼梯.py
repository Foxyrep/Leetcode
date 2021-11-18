#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # 可以转换成斐波那契数列的问题：
        # 跳到n阶台阶上，可以转化为
        # 要么跳到n-1阶上，再跳一阶，这样就有 （跳到n-1阶台阶上的跳法数量） 种跳法
        # 要么跳到n-2阶上，再跳两阶，这样就有 （跳到n-2阶台阶上的跳法数量） 种跳法
        # 因此问题直接转化成斐波那契数列的问题
        # n+1 对应的斐波数 才是 n阶台阶对应的跳法
        '''
        def Fibo(n):
            cur = 0
            nxt = 1
            if n == 0:
                return cur
            if n == 1:
                return nxt
            for i in range(n-1):
                res = cur + nxt
                cur = nxt
                nxt = res
            return res
        return Fibo(n+1)

# @lc code=end

