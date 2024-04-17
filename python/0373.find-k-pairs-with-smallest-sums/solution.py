# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kSmallestPairs(nums1, nums2, k)
    print("\noutput:", serialize(ans, "integer[][]"))
