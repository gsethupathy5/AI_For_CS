# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/design-skiplist/

from typing import *
from leetgo_py import *

# @lc code=begin

class Skiplist:

    def __init__(self):
        

    def search(self, target: int) -> bool:
        

    def add(self, num: int) -> None:
        

    def erase(self, num: int) -> bool:
        

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Skiplist()

    for i in range(1, len(ops)):
        match ops[i]:
            case "search":
                method_params = split_array(params[i])
                target: int = deserialize("int", method_params[0])
                ans = serialize(obj.search(target))
                output.append(ans)
            case "add":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.add(num)
                output.append("null")
            case "erase":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                ans = serialize(obj.erase(num))
                output.append(ans)

    print("\noutput:", join_array(output))
