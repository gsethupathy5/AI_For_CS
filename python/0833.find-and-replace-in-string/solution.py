# Created by asetti2002 at 2024/04/25 19:27
# leetgo: 1.4.3
# https://leetcode.com/problems/find-and-replace-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)
        for i, idx in enumerate(indices):
            if s[idx:].startswith(sources[i]):
                ans[idx:idx + len(sources[i])] = list(targets[i])
        return ''.join(ans)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    indices: List[int] = deserialize("List[int]", read_line())
    sources: List[str] = deserialize("List[str]", read_line())
    targets: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findReplaceString(s, indices, sources, targets)
    print("\noutput:", serialize(ans, "string"))
