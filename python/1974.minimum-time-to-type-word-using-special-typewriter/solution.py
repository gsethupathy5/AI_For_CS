# Created by asetti2002 at 2024/04/25 19:02
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        current = 'a'
        
        for letter in word:
            diff = abs(ord(letter) - ord(current))
            time += min(diff, 26 - diff) + 1
            current = letter
        
        return time
# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().minTimeToType(word)
    print("\noutput:", serialize(ans, "integer"))
