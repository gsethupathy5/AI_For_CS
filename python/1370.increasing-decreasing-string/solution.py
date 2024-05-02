# Created by asetti2002 at 2024/04/25 20:34
# leetgo: 1.4.3
# https://leetcode.com/problems/increasing-decreasing-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortString(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        sorted_counter = sorted(counter.items(), key=lambda x: x[0])
        
        result = []
        while len(result) < len(s):
            for char, count in sorted_counter:
                if count > 0:
                    result.append(char)
                    counter[char] -= 1
            sorted_counter = sorted(counter.items(), key=lambda x: x[0])
            
            for char, count in sorted_counter[::-1]:
                if count > 0:
                    result.append(char)
                    counter[char] -= 1
            sorted_counter = sorted(counter.items(), key=lambda x: x[0])
        
        return "".join(result)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().sortString(s)
    print("\noutput:", serialize(ans, "string"))
