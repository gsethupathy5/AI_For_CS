# Created by asetti2002 at 2024/04/25 20:27
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        import collections
        count = collections.Counter(nums)
        keys = sorted(count)
        for i in keys:
            if count[i] > 0:
                for j in range(1, k):
                    count[i + j] -= count[i]
                    if count[i + j] < 0:
                        return False
        return True
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().isPossibleDivide(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
