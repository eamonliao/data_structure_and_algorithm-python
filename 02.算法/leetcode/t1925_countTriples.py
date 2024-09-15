"""
1925. 统计平方和三元组的数目
一个 平方和三元组 (a,b,c) 指的是满足 a2 + b2 = c2 的 整数 三元组 a，b 和 c 。

给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。
"""


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n+1):
            for b in range(1, n + 1):
                c = int(pow(a*a + b*b + 1, 0.5))
                if c <= n and c*c == a*a + b*b:
                    cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countTriples(5))