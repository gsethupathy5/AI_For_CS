# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/fruit-into-baskets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    fruits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalFruit(fruits)
    print("\noutput:", serialize(ans, "integer"))