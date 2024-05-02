# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/image-overlap/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        pass  # Your code here
# @lc code=end

if __name__ == "__main__":
    img1: List[List[int]] = deserialize("List[List[int]]", read_line())
    img2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestOverlap(img1, img2)
    print("\noutput:", serialize(ans, "integer"))
