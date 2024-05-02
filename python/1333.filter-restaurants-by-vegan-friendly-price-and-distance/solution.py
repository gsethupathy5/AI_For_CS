# Created by asetti2002 at 2024/04/25 20:31
# leetgo: 1.4.3
# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        return [res[0] for res in sorted(filter(lambda x: x[2] >= veganFriendly and x[3] <= maxPrice and x[4] <= maxDistance, restaurants), key=lambda x: (-x[1], -x[0]))]
# @lc code=end

if __name__ == "__main__":
    restaurants: List[List[int]] = deserialize("List[List[int]]", read_line())
    veganFriendly: int = deserialize("int", read_line())
    maxPrice: int = deserialize("int", read_line())
    maxDistance: int = deserialize("int", read_line())
    ans = Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print("\noutput:", serialize(ans, "integer[]"))
