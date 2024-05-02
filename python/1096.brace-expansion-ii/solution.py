# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/brace-expansion-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(s: str) -> Set[str]:
            if '{' not in s:
                return set(s.split(','))
            stack, start = [], -1
            groups = []
            for i, c in enumerate(s):
                if c == '{':
                    if not stack:
                        start = i + 1
                    stack.append(c)
                elif c == '}':
                    stack.pop()
                    if not stack:
                        groups.append(s[start:i])
                elif c == ',' and not stack:
                    groups.append(s[start:i])
                    start = i + 1
            
            return set.union(*[dfs(group) for group in groups])
        
        return sorted(list(dfs(expression)))
# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    ans = Solution().braceExpansionII(expression)
    print("\noutput:", serialize(ans, "string[]"))
