# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-eaten-apples/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    apples: List[int] = deserialize("List[int]", read_line())
    days: List[int] = deserialize("List[int]", read_line())
    ans = Solution().eatenApples(apples, days)
    print("\noutput:", serialize(ans, "integer"))