# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            if not folder[i].startswith(res[-1] + '/'):
                res.append(folder[i])
        return res
# @lc code=end

if __name__ == "__main__":
    folder: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeSubfolders(folder)
    print("\noutput:", serialize(ans, "string[]"))
