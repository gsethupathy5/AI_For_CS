# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    hamsters: str = deserialize("str", read_line())
    ans = Solution().minimumBuckets(hamsters)
    print("\noutput:", serialize(ans, "integer"))
