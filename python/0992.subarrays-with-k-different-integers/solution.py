# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/subarrays-with-k-different-integers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraysWithKDistinct(nums, k)
    print("\noutput:", serialize(ans, "integer"))