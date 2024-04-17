# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[str] = deserialize("List[str]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthDistinct(arr, k)
    print("\noutput:", serialize(ans, "string"))
