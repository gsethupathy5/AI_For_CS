# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    plantTime: List[int] = deserialize("List[int]", read_line())
    growTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().earliestFullBloom(plantTime, growTime)
    print("\noutput:", serialize(ans, "integer"))
