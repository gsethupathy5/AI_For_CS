# Created by asetti2002 at 2024/05/01 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/substring-xor-queries/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        def xor(left, right):
            result = 0
            for i in range(left, right+1):
                result ^= int(s[i])
            return result
        
        ans = []
        for query in queries:
            lefti = -1
            righti = -1
            for i in range(len(s)):
                for j in range(i+1, len(s)+1):
                    if xor(i, j-1) == query[1] ^ query[0]:
                        if lefti == -1 or j-i < righti-lefti:
                            lefti = i
                            righti = j-1
            ans.append([lefti, righti])
        
        return ans
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().substringXorQueries(s, queries)
    print("\noutput:", serialize(ans, "integer[][]"))
