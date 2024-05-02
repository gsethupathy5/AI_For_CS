# Created by asetti2002 at 2024/04/25 19:37
# leetgo: 1.4.3
# https://leetcode.com/problems/bitwise-ors-of-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subarrayBitwiseORs(arr)
    print("\noutput:", serialize(ans, "integer"))
