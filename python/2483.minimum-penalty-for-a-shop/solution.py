# Created by asetti2002 at 2024/05/01 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        def penalty(hours, shop_closed):
            return sum(1 for i, c in enumerate(customers) if (shop_closed and c == 'Y') or (not shop_closed and c == 'N'))

        n = len(customers)
        left, right = 0, n
        
        while left < right:
            mid = left + (right - left) // 2
            if penalty(mid, shop_closed=False) < penalty(mid, shop_closed=True):
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end

if __name__ == "__main__":
    customers: str = deserialize("str", read_line())
    ans = Solution().bestClosingTime(customers)
    print("\noutput:", serialize(ans, "integer"))
