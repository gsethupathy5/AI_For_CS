# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-candies-to-people/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    candies: int = deserialize("int", read_line())
    num_people: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(candies, num_people)
    print("\noutput:", serialize(ans, "integer[]"))
