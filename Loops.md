# Loops
## Task
The provided code stub read an integer `n` from STDIN. For all non-negative integers `i < n`, print **i<sup>2</sup>**.

#### Input Format

The first and only line contains the integer, `n`.

#### Constraints
1 <= n <= 20

#### Output Format

Print `n` lines, one corresponding to each `i`.

```
Sample Input :
5
```

```
Sample Output :
0
1
4
9
16
```

#### Given Code

```python
if __name__ == '__main__':
    n = int(input())
```

## Solution

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)
```
