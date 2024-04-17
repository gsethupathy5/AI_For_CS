# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/image-smoother/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    img: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().imageSmoother(img)
    print("\noutput:", serialize(ans, "integer[][]"))
