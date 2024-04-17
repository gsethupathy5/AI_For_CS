# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().sumOfThree(num)
    print("\noutput:", serialize(ans, "long[]"))
