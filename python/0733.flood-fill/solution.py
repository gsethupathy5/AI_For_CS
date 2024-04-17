# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/flood-fill/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    image: List[List[int]] = deserialize("List[List[int]]", read_line())
    sr: int = deserialize("int", read_line())
    sc: int = deserialize("int", read_line())
    color: int = deserialize("int", read_line())
    ans = Solution().floodFill(image, sr, sc, color)
    print("\noutput:", serialize(ans, "integer[][]"))
