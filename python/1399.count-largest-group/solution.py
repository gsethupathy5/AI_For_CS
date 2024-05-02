# Created by asetti2002 at 2024/04/25 20:37
# leetgo: 1.4.3
# https://leetcode.com/problems/count-largest-group/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            return sum([int(i) for i in str(num)])

        group_size = {}
        for i in range(1, n+1):
            sum_digit = digit_sum(i)
            group_size[sum_digit] = group_size.get(sum_digit, 0) + 1

        max_count = max(group_size.values())
        return list(group_size.values()).count(max_count)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countLargestGroup(n)
    print("\noutput:", serialize(ans, "integer"))
