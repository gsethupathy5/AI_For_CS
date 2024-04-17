# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxChunksToSorted(arr)
    print("\noutput:", serialize(ans, "integer"))
