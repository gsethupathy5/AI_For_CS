# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += abs(nums[i] - target[i]) // 2
        return res
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makeSimilar(nums, target)
    print("\noutput:", serialize(ans, "long"))
