# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    group: List[int] = deserialize("List[int]", read_line())
    beforeItems: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sortItems(n, m, group, beforeItems)
    print("\noutput:", serialize(ans, "integer[]"))
