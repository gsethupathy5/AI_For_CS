# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/tweet-counts-per-frequency/

from typing import *
from leetgo_py import *

# @lc code=begin

class TweetCounts:

    def __init__(self):
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = TweetCounts()

    for i in range(1, len(ops)):
        match ops[i]:
            case "recordTweet":
                method_params = split_array(params[i])
                tweetName: str = deserialize("str", method_params[0])
                time: int = deserialize("int", method_params[1])
                obj.recordTweet(tweetName, time)
                output.append("null")
            case "getTweetCountsPerFrequency":
                method_params = split_array(params[i])
                freq: str = deserialize("str", method_params[0])
                tweetName: str = deserialize("str", method_params[1])
                startTime: int = deserialize("int", method_params[2])
                endTime: int = deserialize("int", method_params[3])
                ans = serialize(obj.getTweetCountsPerFrequency(freq, tweetName, startTime, endTime))
                output.append(ans)

    print("\noutput:", join_array(output))
