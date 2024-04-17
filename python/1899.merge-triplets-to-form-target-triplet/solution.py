# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    triplets: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mergeTriplets(triplets, target)
    print("\noutput:", serialize(ans, "boolean"))
