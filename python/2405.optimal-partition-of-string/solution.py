# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/optimal-partition-of-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def partitionString(self, s: str) -> int:
        def get_unique_substrings(s):
            seen = set()
            substrings = []
            current_substring = ""
            
            for char in s:
                if char in seen:
                    substrings.append(current_substring)
                    current_substring = ""
                    seen = set()
                
                seen.add(char)
                current_substring += char
            
            substrings.append(current_substring)
            return len(substrings)
        
        return get_unique_substrings(s)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionString(s)
    print("\noutput:", serialize(ans, "integer"))
