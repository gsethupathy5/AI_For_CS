# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count('a') < k or s.count('b') < k or s.count('c') < k:
            return -1
        diff_a = s.count('a') - k
        diff_b = s.count('b') - k
        diff_c = s.count('c') - k
        moves = 0
        i, j = 0, len(s) - 1
        while i < j:
            if diff_a <= 0 and diff_b <= 0 and diff_c <= 0:
                break
            if s[i] == 'a':
                diff_a -= 1
            elif s[i] == 'b':
                diff_b -= 1
            else:
                diff_c -= 1
            if s[j] == 'a':
                diff_a -= 1
            elif s[j] == 'b':
                diff_b -= 1
            else:
                diff_c -= 1
            moves += 1
            i += 1
            j -= 1
        return moves
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().takeCharacters(s, k)
    print("\noutput:", serialize(ans, "integer"))
