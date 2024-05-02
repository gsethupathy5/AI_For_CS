# Created by asetti2002 at 2024/04/25 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-values-from-labels/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        from collections import Counter
        from heapq import nlargest
        
        label_counter = Counter()
        subset = []
        score = 0
        
        for val, label in sorted(zip(values, labels), reverse=True):
            if label_counter[label] < useLimit:
                subset.append(val)
                label_counter[label] += 1
                score += val
                if len(subset) == numWanted:
                    break
                    
        return score
# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    labels: List[int] = deserialize("List[int]", read_line())
    numWanted: int = deserialize("int", read_line())
    useLimit: int = deserialize("int", read_line())
    ans = Solution().largestValsFromLabels(values, labels, numWanted, useLimit)
    print("\noutput:", serialize(ans, "integer"))
