# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

from typing import *
from leetgo_py import *

# @lc code=begin

class RandomizedCollection:

    def __init__(self):
        

    def insert(self, val: int) -> bool:
        

    def remove(self, val: int) -> bool:
        

    def getRandom(self) -> int:
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = RandomizedCollection()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.insert(val))
                output.append(ans)
            case "remove":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                ans = serialize(obj.remove(val))
                output.append(ans)
            case "getRandom":
                ans = serialize(obj.getRandom())
                output.append(ans)

    print("\noutput:", join_array(output))
