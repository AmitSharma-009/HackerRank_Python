# Find the Runner-Up Score
## Problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up `n` score. You are given  scores. Store them in a list and find the score of the runner-up.


#### Input Format

The first line contains `n`. The second line contains an array `A[]`  of `n` integers each separated by a space.


#### Constraints
2 <= n <= 10
-100 <= A[i] <= 100

#### Output Format

Print the runner-up score.

```
Sample Input :
5
2 3 6 6 5
```

```
Sample Output :
5
```

#### Explanation
Given list is `[2,3,6,6,5]`. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.


#### Given Code

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
```


## Solution 1

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(set(arr), reverse=True)[1])
```


## Solution 2

```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = max(arr)
    a = None

    for num in arr:
        if num == max:
            pass
        elif a == None:
            a = num
        elif num > a:
            a = num

    print(a)
```
