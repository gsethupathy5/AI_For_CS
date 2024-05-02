# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        
        res = []
        
        for query in queries:
            count = 0
            f_query = f(query)
            for word in words:
                if f_query < f(word):
                    count += 1
            res.append(count)
        
        return res
# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSmallerByFrequency(queries, words)
    print("\noutput:", serialize(ans, "integer[]"))
