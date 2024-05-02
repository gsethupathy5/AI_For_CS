# Created by asetti2002 at 2024/05/01 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumReplacement(nums)
    print("\noutput:", serialize(ans, "long"))
