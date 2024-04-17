# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().uniqueOccurrences(arr)
    print("\noutput:", serialize(ans, "boolean"))
