# [436. Find Right Interval][link] (Medium)

[link]: https://leetcode.com/problems/find-right-interval/

You are given an array of `intervals`, where `intervals[i] = [startᵢ, endᵢ]` and each `startᵢ` is
**unique**.

The **right interval** for an interval `i` is an interval `j` such that `startⱼ >= endᵢ` and
`startⱼ` is **minimized**. Note that `i` may equal `j`.

Return an array of **right interval** indices for each interval `i`. If no **right interval** exists
for interval `i`, then put `-1` at index `i`.

**Example 1:**

```
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.
```

**Example 2:**

```
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start₀ = 3 is the smallest start that is >= end₁ = 3.
The right interval for [1,2] is [2,3] since start₁ = 2 is the smallest start that is >= end₂ = 2.
```

**Example 3:**

```
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start₂ = 3 is the smallest start that is >= end₁ = 3.
```

**Constraints:**

- `1 <= intervals.length <= 2 * 10⁴`
- `intervals[i].length == 2`
- `-10⁶ <= startᵢ <= endᵢ <= 10⁶`
- The start point of each interval is **unique**.
