# Created by asetti2002 at 2024/05/01 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/most-popular-video-creator/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        from collections import defaultdict
        
        creator_views = defaultdict(int)
        video_dict = defaultdict(list)
        
        for i in range(len(creators)):
            creator_views[creators[i]] += views[i]
            video_dict[creators[i]].append((ids[i], views[i]))
        
        max_views = max(creator_views.values())
        
        result = []
        for creator, total_views in creator_views.items():
            if total_views == max_views:
                videos = video_dict[creator]
                top_video = min(videos, key=lambda x: x[0])[0]
                result.append([creator, top_video])
        
        return result
# @lc code=end

if __name__ == "__main__":
    creators: List[str] = deserialize("List[str]", read_line())
    ids: List[str] = deserialize("List[str]", read_line())
    views: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostPopularCreator(creators, ids, views)
    print("\noutput:", serialize(ans, "string[][]"))
