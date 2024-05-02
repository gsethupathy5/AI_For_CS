# Created by asetti2002 at 2024/04/25 20:22
# leetgo: 1.4.3
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def is_palindrome(n):
            return str(n) == str(n)[::-1]

        result = []
        for query in queries:
            count = 0
            for i in range(10 ** (intLength - 1), 10 ** intLength):
                if is_palindrome(i):
                    count += 1
                if count == query:
                    result.append(i)
                    break
            if count < query:
                result.append(-1)

        return result
# @lc code=end

if __name__ == "__main__":
    queries: List[int] = deserialize("List[int]", read_line())
    intLength: int = deserialize("int", read_line())
    ans = Solution().kthPalindrome(queries, intLength)
    print("\noutput:", serialize(ans, "long[]"))
