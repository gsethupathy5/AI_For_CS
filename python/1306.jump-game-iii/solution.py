# Created by asetti2002 at 2024/04/25 20:28
# leetgo: 1.4.3
# https://leetcode.com/problems/jump-game-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(index):
            if 0 <= index < len(arr) and arr[index] >= 0:
                if arr[index] == 0:
                    return True
                arr[index] = -arr[index]
                return dfs(index + arr[index]) or dfs(index - arr[index])
            return False
        
        return dfs(start)
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().canReach(arr, start)
    print("\noutput:", serialize(ans, "boolean"))
