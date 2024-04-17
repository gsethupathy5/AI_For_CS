# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/jewels-and-stones/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    jewels: str = deserialize("str", read_line())
    stones: str = deserialize("str", read_line())
    ans = Solution().numJewelsInStones(jewels, stones)
    print("\noutput:", serialize(ans, "integer"))
