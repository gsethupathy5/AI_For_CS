# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/design-hashset/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyHashSet:

    def __init__(self):
        

    def add(self, key: int) -> None:
        

    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.add(key)
                output.append("null")
            case "remove":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.remove(key)
                output.append("null")
            case "contains":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.contains(key))
                output.append(ans)

    print("\noutput:", join_array(output))
