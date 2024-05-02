# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        import itertools
        l = list(itertools.product('abc', repeat=n))
        happy_strings = []
        for s in l:
            if all(s[i] != s[i + 1] for i in range(len(s) - 1)):
                happy_strings.append(''.join(s))
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getHappyString(n, k)
    print("\noutput:", serialize(ans, "string"))
