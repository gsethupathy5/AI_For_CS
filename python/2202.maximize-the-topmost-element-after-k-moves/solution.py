# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        # Write your code here
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumTop(nums, k)
    print("\noutput:", serialize(ans, "integer"))
