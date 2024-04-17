# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

from typing import *
from leetgo_py import *

# @lc code=begin

class SORTracker:

    def __init__(self):
        

    def add(self, name: str, score: int) -> None:
        

    def get(self) -> str:
        

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = SORTracker()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                score: int = deserialize("int", method_params[1])
                obj.add(name, score)
                output.append("null")
            case "get":
                ans = serialize(obj.get())
                output.append(ans)

    print("\noutput:", join_array(output))
