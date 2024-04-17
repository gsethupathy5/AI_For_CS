# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/destination-city/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    paths: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().destCity(paths)
    print("\noutput:", serialize(ans, "string"))
