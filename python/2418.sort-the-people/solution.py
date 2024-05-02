# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-people/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), key=lambda x: x[0], reverse=True]
# @lc code=end

if __name__ == "__main__":
    names: List[str] = deserialize("List[str]", read_line())
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortPeople(names, heights)
    print("\noutput:", serialize(ans, "string[]"))
