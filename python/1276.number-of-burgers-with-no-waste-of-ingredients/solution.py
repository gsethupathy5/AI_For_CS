# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    tomatoSlices: int = deserialize("int", read_line())
    cheeseSlices: int = deserialize("int", read_line())
    ans = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
    print("\noutput:", serialize(ans, "integer[]"))
