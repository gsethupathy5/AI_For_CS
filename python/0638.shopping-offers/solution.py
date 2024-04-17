# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/shopping-offers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    price: List[int] = deserialize("List[int]", read_line())
    special: List[List[int]] = deserialize("List[List[int]]", read_line())
    needs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().shoppingOffers(price, special, needs)
    print("\noutput:", serialize(ans, "integer"))
