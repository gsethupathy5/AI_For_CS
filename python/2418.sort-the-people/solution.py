# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-people/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    names: List[str] = deserialize("List[str]", read_line())
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortPeople(names, heights)
    print("\noutput:", serialize(ans, "string[]"))
