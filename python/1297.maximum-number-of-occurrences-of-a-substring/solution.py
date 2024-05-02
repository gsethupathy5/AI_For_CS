# Created by asetti2002 at 2024/04/25 20:28
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import Counter
        def count_unique(s):
            return len(set(s))
        ans = 0
        limit = Counter()
        substr_counts = Counter()
        for i in range(0, len(s) - minSize + 1):
            cur_substr = s[i: i + minSize]
            if count_unique(cur_substr) <= maxLetters:
                substr_counts[cur_substr] += 1
                limit[substr_counts[cur_substr]] += 1
                ans = max(ans, substr_counts[cur_substr])
        return ans
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    maxLetters: int = deserialize("int", read_line())
    minSize: int = deserialize("int", read_line())
    maxSize: int = deserialize("int", read_line())
    ans = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print("\noutput:", serialize(ans, "integer"))
