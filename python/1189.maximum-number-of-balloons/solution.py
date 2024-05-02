# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-balloons/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counts = Counter(text)
        return min(counts['b'], counts['a'], counts['l']//2, counts['o']//2, counts['n'])
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().maxNumberOfBalloons(text)
    print("\noutput:", serialize(ans, "integer"))
