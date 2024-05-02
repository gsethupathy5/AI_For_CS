# Created by asetti2002 at 2024/04/25 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/validate-binary-tree-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {i: i for i in range(n)}
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1:
                if find(l) == find(i):
                    return False
                union(i, l)
            if r != -1:
                if find(r) == find(i):
                    return False
                union(i, r)
        
        root_set = set()
        for i in range(n):
            root_set.add(find(i))
        
        return len(root_set) == 1 and root_set.pop() == 0
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    leftChild: List[int] = deserialize("List[int]", read_line())
    rightChild: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)
    print("\noutput:", serialize(ans, "boolean"))
