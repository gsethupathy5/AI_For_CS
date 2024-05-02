# Created by asetti2002 at 2024/04/25 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        def extractArtifact(artifact):
            nonlocal artifacts_uncovered
            for r in range(artifact[0], artifact[2]+1):
                for c in range(artifact[1], artifact[3]+1):
                    if grid[r][c] == 0:
                        return
            artifacts_uncovered.remove(artifact)

        grid = [[0 for _ in range(n)] for _ in range(n)]
        artifacts_uncovered = [artifact for artifact in artifacts]

        for r, c in dig:
            grid[r][c] = 1
            for artifact in artifacts_uncovered[:]:
                if artifact[0] <= r <= artifact[2] and artifact[1] <= c <= artifact[3]:
                    extractArtifact(artifact)

        return len(artifacts) - len(artifacts_uncovered)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    artifacts: List[List[int]] = deserialize("List[List[int]]", read_line())
    dig: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().digArtifacts(n, artifacts, dig)
    print("\noutput:", serialize(ans, "integer"))
