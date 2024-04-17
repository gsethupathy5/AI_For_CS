# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/most-beautiful-item-for-each-query/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    items: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumBeauty(items, queries)
    print("\noutput:", serialize(ans, "integer[]"))
