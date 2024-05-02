# Created by asetti2002 at 2024/04/25 20:32
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        start = 0
        seen = {'a': 0, 'b': 0, 'c': 0}
        
        for end, char in enumerate(s):
            seen[char] += 1
            
            while all(seen.values()):
                count += len(s) - end
                seen[s[start]] -= 1
                start += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfSubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
