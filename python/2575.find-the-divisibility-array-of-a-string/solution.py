# Created by asetti2002 at 2024/05/01 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        prefix = 0
        for i in range(len(word)):
            prefix = (prefix * 10 + int(word[i])) % m
            res.append(1 if prefix == 0 else 0)
        return res
# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().divisibilityArray(word, m)
    print("\noutput:", serialize(ans, "integer[]"))
