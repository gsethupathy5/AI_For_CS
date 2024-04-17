# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    pizza: List[str] = deserialize("List[str]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().ways(pizza, k)
    print("\noutput:", serialize(ans, "integer"))
