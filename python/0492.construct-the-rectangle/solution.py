# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-the-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    area: int = deserialize("int", read_line())
    ans = Solution().constructRectangle(area)
    print("\noutput:", serialize(ans, "integer[]"))
