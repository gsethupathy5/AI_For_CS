# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/strange-printer-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    targetGrid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isPrintable(targetGrid)
    print("\noutput:", serialize(ans, "boolean"))
