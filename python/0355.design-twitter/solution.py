# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/design-twitter/

from typing import *
from leetgo_py import *

# @lc code=begin

class Twitter:

    def __init__(self):
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Twitter()

    for i in range(1, len(ops)):
        match ops[i]:
            case "postTweet":
                method_params = split_array(params[i])
                userId: int = deserialize("int", method_params[0])
                tweetId: int = deserialize("int", method_params[1])
                obj.postTweet(userId, tweetId)
                output.append("null")
            case "getNewsFeed":
                method_params = split_array(params[i])
                userId: int = deserialize("int", method_params[0])
                ans = serialize(obj.getNewsFeed(userId))
                output.append(ans)
            case "follow":
                method_params = split_array(params[i])
                followerId: int = deserialize("int", method_params[0])
                followeeId: int = deserialize("int", method_params[1])
                obj.follow(followerId, followeeId)
                output.append("null")
            case "unfollow":
                method_params = split_array(params[i])
                followerId: int = deserialize("int", method_params[0])
                followeeId: int = deserialize("int", method_params[1])
                obj.unfollow(followerId, followeeId)
                output.append("null")

    print("\noutput:", join_array(output))
