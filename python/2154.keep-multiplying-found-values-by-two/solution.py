# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    original: int = deserialize("int", read_line())
    ans = Solution().findFinalValue(nums, original)
    print("\noutput:", serialize(ans, "integer"))
