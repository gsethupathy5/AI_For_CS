# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/find-k-closest-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findClosestElements(arr, k, x)
    print("\noutput:", serialize(ans, "integer[]"))
