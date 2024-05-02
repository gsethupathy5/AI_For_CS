# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        def to_decimal(binary):
            return int(binary, 2)

        def to_binary(decimal):
            return bin(decimal)[2:]

        def is_subsequence(sub, target):
            i = 0
            for j in range(len(target)):
                if i < len(sub) and sub[i] == target[j]:
                    i += 1
            return i == len(sub)

        max_len = 0
        for i in range(1, 2 ** len(s)):
            binary = to_binary(i)
            if is_subsequence(binary, s) and to_decimal(binary) <= k:
                max_len = max(max_len, len(binary))

        return max_len
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestSubsequence(s, k)
    print("\noutput:", serialize(ans, "integer"))
