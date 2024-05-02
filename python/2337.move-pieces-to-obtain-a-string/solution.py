# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def count_steps(s):
            count = 0
            for i in range(len(s) - 1):
                if s[i] == 'R' and s[i+1] == '_':
                    count += 1
            return count
        
        return count_steps(start) >= count_steps(target) and start.count('L') >= target.count('L')
# @lc code=end

if __name__ == "__main__":
    start: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().canChange(start, target)
    print("\noutput:", serialize(ans, "boolean"))
