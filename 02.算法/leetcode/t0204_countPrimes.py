"""
204. 计数质数
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
"""


class Solution:
    def isPrimes(self, n: int) -> bool:
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        prime_cnt = 0
        for i in range(2, n):
            if self.isPrimes(i):
                prime_cnt += 1

        return prime_cnt
