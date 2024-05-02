# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
            rev_num = int(str(num)[::-1])
            seen.add(rev_num)
        return len(seen)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countDistinctIntegers(nums)
    print("\noutput:", serialize(ans, "integer"))
