# Created by asetti2002 at 2024/05/01 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().partitionArray(nums, k)
    print("\noutput:", serialize(ans, "integer"))
