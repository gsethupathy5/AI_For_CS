# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/the-k-strongest-values-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getStrongest(arr, k)
    print("\noutput:", serialize(ans, "integer[]"))
