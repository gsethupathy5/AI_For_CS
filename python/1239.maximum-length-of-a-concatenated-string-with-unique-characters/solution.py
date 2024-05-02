# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, path):
            if len(set(path)) != len(path):
                return
            nonlocal max_length
            max_length = max(max_length, len(path))
            if index == len(arr):
                return
            for i in range(index, len(arr)):
                backtrack(i + 1, path + arr[i])
        
        max_length = 0
        backtrack(0, '')
        return max_length
# @lc code=end

if __name__ == "__main__":
    arr: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxLength(arr)
    print("\noutput:", serialize(ans, "integer"))
