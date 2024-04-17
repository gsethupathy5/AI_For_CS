# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    status: List[int] = deserialize("List[int]", read_line())
    candies: List[int] = deserialize("List[int]", read_line())
    keys: List[List[int]] = deserialize("List[List[int]]", read_line())
    containedBoxes: List[List[int]] = deserialize("List[List[int]]", read_line())
    initialBoxes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print("\noutput:", serialize(ans, "integer"))
