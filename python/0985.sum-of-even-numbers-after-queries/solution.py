# Created by asetti2002 at 2024/04/25 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            res.append(even_sum)
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sumEvenAfterQueries(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
