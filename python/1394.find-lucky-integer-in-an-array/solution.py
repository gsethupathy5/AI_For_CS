# Created by asetti2002 at 2024/04/25 20:38
# leetgo: 1.4.3
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        count = Counter(arr)
        result = -1
        for key, value in count.items():
            if key == value:
                result = max(result, key)
        return result
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLucky(arr)
    print("\noutput:", serialize(ans, "integer"))
