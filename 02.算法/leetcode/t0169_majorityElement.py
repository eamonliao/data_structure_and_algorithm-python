"""
https://leetcode.cn/problems/majority-element/
169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3] 输出：3
示例 2：
输入：nums = [2,2,1,1,1,2,2] 输出：2

提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res_map = {}
        for i in nums:
            if i not in res_map.keys():
                res_map[i] = 1
            else:
                res_map[i] += 1

            if res_map[i] > len(nums) / 2:
                return i

        return None