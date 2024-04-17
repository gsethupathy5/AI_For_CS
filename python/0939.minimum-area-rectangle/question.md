# [939. Minimum Area Rectangle][link] (Medium)

[link]: https://leetcode.com/problems/minimum-area-rectangle/

You are given an array of points in the **X-Y** plane `points` where `points[i] = [xᵢ, yᵢ]`.

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y
axes. If there is not any such rectangle, return `0`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

**Constraints:**

- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= xᵢ, yᵢ <= 4 * 10⁴`
- All the given points are **unique**.
