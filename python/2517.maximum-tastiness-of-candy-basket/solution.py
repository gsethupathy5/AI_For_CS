# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    price: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumTastiness(price, k)
    print("\noutput:", serialize(ans, "integer"))
