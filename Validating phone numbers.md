# Validating phone numbers
## Problem

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7,8 or 9.

## Concept

A valid mobile number is a ten digit number starting with a 7,8 or 9.
Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

#### Input Format

The first line contains an integer N, the number of inputs. N lines follow, each containing some string.

#### Constraints

1 <= `N` <= 10
2 <= `len(Number)` <= 15

#### Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

**Sample Input 0**

```
2
9587456281
1252478965
```

**Sample Output 0**

```
YES
NO
```

## Solution

```python
import re

N = int(input())
for i in range(0, N):
    # Must start with a 7, 8, or 9 according to the problem, must only contain 10 digits total
    print('YES') if re.match(r'[789]\d{9}$', input()) else print('NO') 
```
