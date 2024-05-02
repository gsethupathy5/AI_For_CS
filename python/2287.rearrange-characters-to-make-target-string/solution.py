# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        import collections
        
        if len(target) == 0:
            return 0
        
        target_counter = collections.Counter(target)
        max_copies = 0
        
        for i in range(len(target), len(s)+1):
            if collections.Counter(s[i-len(target):i]) == target_counter:
                max_copies += 1
                
        return max_copies
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().rearrangeCharacters(s, target)
    print("\noutput:", serialize(ans, "integer"))
