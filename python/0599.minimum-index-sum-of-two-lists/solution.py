# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    list1: List[str] = deserialize("List[str]", read_line())
    list2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findRestaurant(list1, list2)
    print("\noutput:", serialize(ans, "string[]"))
