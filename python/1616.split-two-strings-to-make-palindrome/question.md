# [1616. Split Two Strings to Make Palindrome][link] (Medium)

[link]: https://leetcode.com/problems/split-two-strings-to-make-palindrome/

You are given two strings `a` and `b` of the same length. Choose an index and split both strings
**at the same index**, splitting `a` into two strings: `aₚᵣₑfᵢₓ` and `aₛᵤffᵢₓ` where `a = aₚᵣₑfᵢₓ +
aₛᵤffᵢₓ`, and splitting `b` into two strings: `bₚᵣₑfᵢₓ` and `bₛᵤffᵢₓ` where `b = bₚᵣₑfᵢₓ + bₛᵤffᵢₓ`.
Check if `aₚᵣₑfᵢₓ + bₛᵤffᵢₓ` or `bₚᵣₑfᵢₓ + aₛᵤffᵢₓ` forms a palindrome.

When you split a string `s` into `sₚᵣₑfᵢₓ` and `sₛᵤffᵢₓ`, either `sₛᵤffᵢₓ` or `sₚᵣₑfᵢₓ` is allowed
to be empty. For example, if `s = "abc"`, then `"" + "abc"`, `"a" + "bc"`, `"ab" + "c"` , and `"abc"
+ ""` are valid splits.

Return `true` if it is possible to form a palindrome string, otherwise return  `false`.

**Notice** that `x + y` denotes the concatenation of strings `x` and `y`.

**Example 1:**

```
Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the
following way:
aₚᵣₑfᵢₓ = "", aₛᵤffᵢₓ = "x"
bₚᵣₑfᵢₓ = "", bₛᵤffᵢₓ = "y"
Then, aₚᵣₑfᵢₓ + bₛᵤffᵢₓ = "" + "y" = "y", which is a palindrome.
```

**Example 2:**

```
Input: a = "xbdef", b = "xecab"
Output: false
```

**Example 3:**

```
Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aₚᵣₑfᵢₓ = "ula", aₛᵤffᵢₓ = "cfd"
bₚᵣₑfᵢₓ = "jiz", bₛᵤffᵢₓ = "alu"
Then, aₚᵣₑfᵢₓ + bₛᵤffᵢₓ = "ula" + "alu" = "ulaalu", which is a palindrome.
```

**Constraints:**

- `1 <= a.length, b.length <= 10⁵`
- `a.length == b.length`
- `a` and `b` consist of lowercase English letters
