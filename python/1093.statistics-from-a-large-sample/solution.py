# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/statistics-from-a-large-sample/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        

# @lc code=end

if __name__ == "__main__":
    count: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sampleStats(count)
    print("\noutput:", serialize(ans, "double[]"))
