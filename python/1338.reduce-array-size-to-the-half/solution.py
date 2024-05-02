# Created by asetti2002 at 2024/04/25 20:33
# leetgo: 1.4.3
# https://leetcode.com/problems/reduce-array-size-to-the-half/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        count = Counter(arr)
        sorted_count = sorted(count.values(), reverse=True)
        total = len(arr)
        target = total // 2
        ans = 0
        removed = 0
        for num in sorted_count:
            removed += num
            ans += 1
            if removed >= target:
                return ans
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSetSize(arr)
    print("\noutput:", serialize(ans, "integer"))
