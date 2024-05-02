# Created by asetti2002 at 2024/04/25 19:29
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-mountain-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = base = 0

        while base < n:
            end = base
            if end + 1 < n and arr[end] < arr[end + 1]:
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1

                if end + 1 < n and arr[end] > arr[end + 1]:
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    ans = max(ans, end - base + 1)
                else:
                    end += 1

            base = max(end, base + 1)

        return ans
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestMountain(arr)
    print("\noutput:", serialize(ans, "integer"))
