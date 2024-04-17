# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/describe-the-painting/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    segments: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().splitPainting(segments)
    print("\noutput:", serialize(ans, "long[][]"))
