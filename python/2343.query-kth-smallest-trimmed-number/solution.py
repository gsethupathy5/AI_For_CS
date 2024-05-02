# Created by asetti2002 at 2024/05/01 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def trim_number(number, trim):
            return number[-trim:]

        result = []
        for query in queries:
            ki, trimi = query[0], query[1]
            trimmed_nums = [trim_number(num, trimi) for num in nums]
            sorted_indices = sorted(range(len(trimmed_nums)), key=lambda x: (trimmed_nums[x], x))
            result.append(sorted_indices.index(ki))

        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[str] = deserialize("List[str]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().smallestTrimmedNumbers(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
