# Created by asetti2002 at 2024/04/25 20:37
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-k-palindrome-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
        return odd_count <= k <= len(s)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().canConstruct(s, k)
    print("\noutput:", serialize(ans, "boolean"))
