# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if (tomatoSlices - 2 * cheeseSlices) % 2 != 0 or (4 * cheeseSlices - tomatoSlices) % 2 != 0 or tomatoSlices < 0 or cheeseSlices < 0:
            return []
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = (4 * cheeseSlices - tomatoSlices) // 2
        if jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
# @lc code=end

if __name__ == "__main__":
    tomatoSlices: int = deserialize("int", read_line())
    cheeseSlices: int = deserialize("int", read_line())
    ans = Solution().numOfBurgers(tomatoSlices, cheeseSlices)
    print("\noutput:", serialize(ans, "integer[]"))
