# Print Function
## Task
The included code stub will read an integer `n` from STDIN.

Without using any string methods, try to print the following:
`123...N`

Note that "..." represents the values in between.

#### Input Format

The first line contains an integer `n`.


#### Output Format

Output the answer as explained in the task.

```
Sample Input :
3
```

```
Sample Output :
123
```


#### Given Code

```python
if __name__ == '__main__':
    n = int(input())
```

----

## Solution

```python
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep="")
```
