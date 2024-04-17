# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/design-browser-history/

from typing import *
from leetgo_py import *

# @lc code=begin

class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    homepage: str = deserialize("str", constructor_params[0])
    obj = BrowserHistory(homepage)

    for i in range(1, len(ops)):
        match ops[i]:
            case "visit":
                method_params = split_array(params[i])
                url: str = deserialize("str", method_params[0])
                obj.visit(url)
                output.append("null")
            case "back":
                method_params = split_array(params[i])
                steps: int = deserialize("int", method_params[0])
                ans = serialize(obj.back(steps))
                output.append(ans)
            case "forward":
                method_params = split_array(params[i])
                steps: int = deserialize("int", method_params[0])
                ans = serialize(obj.forward(steps))
                output.append(ans)

    print("\noutput:", join_array(output))
