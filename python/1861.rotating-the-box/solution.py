# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/rotating-the-box/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    box: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().rotateTheBox(box)
    print("\noutput:", serialize(ans, "character[][]"))
