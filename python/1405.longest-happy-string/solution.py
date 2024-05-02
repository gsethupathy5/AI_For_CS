# Created by asetti2002 at 2024/04/25 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-happy-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        while True:
            cnt, char = heapq.heappop(pq)
            if cnt == 0:
                break
            if res[-2:] == char * 2:
                if not pq:
                    break
                cnt2, char2 = heapq.heappop(pq)
                res += char2 * min(cnt2, 1)
                if cnt2 + 1 < 0:
                    heapq.heappush(pq, (cnt2 + 1, char2))
                heapq.heappush(pq, (cnt, char))
            else:
                res += char * min(cnt, 2)
                if cnt + 1 < 0:
                    heapq.heappush(pq, (cnt + 1, char))
        return res
# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().longestDiverseString(a, b, c)
    print("\noutput:", serialize(ans, "string"))
