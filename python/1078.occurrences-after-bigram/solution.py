# Created by asetti2002 at 2024/04/25 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/occurrences-after-bigram/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = []
        
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        
        return result
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    first: str = deserialize("str", read_line())
    second: str = deserialize("str", read_line())
    ans = Solution().findOcurrences(text, first, second)
    print("\noutput:", serialize(ans, "string[]"))
