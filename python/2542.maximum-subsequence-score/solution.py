# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-subsequence-score/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
