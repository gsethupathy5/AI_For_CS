# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/distant-barcodes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import collections
        pq = [(-v, k) for k, v in collections.Counter(barcodes).items()]
        heapq.heapify(pq)
        res = []
        while len(pq) > 1:
            (v1, k1), (v2, k2) = heapq.heappop(pq), heapq.heappop(pq)
            res.extend([k1, k2])
            if v1 + 1: heapq.heappush(pq, (v1 + 1, k1))
            if v2 + 1: heapq.heappush(pq, (v2 + 1, k2))
        return res + [pq[0][1]] if pq else res
# @lc code=end

if __name__ == "__main__":
    barcodes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rearrangeBarcodes(barcodes)
    print("\noutput:", serialize(ans, "integer[]"))
