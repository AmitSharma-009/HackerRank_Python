# Division
## Task
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain integer division,  `a` // `b` . The second line should contain float division,  `a`/`b` .

No rounding or formatting is necessary.

#### Input Format

The first line contains the first integer, `a`. The second line contains the second integer, `b`.


#### Output Format

Print the two lines as described above.

```
Sample Input :
4
3
```

```
Sample Output :
1
1.33333333333
```

#### Given Code

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
```

## Solution

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(int(a / b))
    print(float(a / b))
```
