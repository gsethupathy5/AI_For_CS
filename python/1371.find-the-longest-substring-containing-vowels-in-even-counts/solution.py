# Created by asetti2002 at 2024/04/25 20:34
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state = [0] + [-1] * 31
        res, curr_state = 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                curr_state ^= 1 << vowels[c]
            if state[curr_state] >= 0:
                res = max(res, i + 1 - state[curr_state])
            else:
                state[curr_state] = i + 1
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findTheLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
