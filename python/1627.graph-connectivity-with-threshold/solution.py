# Created by asetti2002 at 2024/04/25 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/graph-connectivity-with-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        def find_parent(parent, u):
            if parent[u] != u:
                return find_parent(parent, parent[u])
            return parent[u]

        def union(parent, rank, u, v):
            u_root = find_parent(parent, u)
            v_root = find_parent(parent, v)

            if rank[u_root] < rank[v_root]:
                parent[u_root] = v_root
            elif rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
            else:
                parent[v_root] = u_root
                rank[u_root] += 1

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        for i in range(threshold + 1, n + 1):
            for j in range(i * 2, n + 1, i):
                if gcd(i, j) > threshold:
                    union(parent, rank, i, j)

        result = []
        for query in queries:
            a, b = query
            if find_parent(parent, a) == find_parent(parent, b):
                result.append(True)
            else:
                result.append(False)

        return result
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().areConnected(n, threshold, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
