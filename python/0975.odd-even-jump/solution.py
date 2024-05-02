# Created by asetti2002 at 2024/04/25 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/odd-even-jump/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # Add your code here
        pass
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().oddEvenJumps(arr)
    print("\noutput:", serialize(ans, "integer"))
