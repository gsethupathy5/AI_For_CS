# [149. Max Points on a Line][link] (Hard)

[link]: https://leetcode.com/problems/max-points-on-a-line/

Given an array of `points` where `points[i] = [xᵢ, yᵢ]` represents a point on the **X-Y** plane,
return the maximum number of points that lie on the same straight line.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10⁴ <= xᵢ, yᵢ <= 10⁴`
- All the `points` are **unique**.
