# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().replaceElements(arr)
    print("\noutput:", serialize(ans, "integer[]"))