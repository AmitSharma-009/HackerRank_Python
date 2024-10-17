"""
Find the Runner-Up Score!

Code:
"""

#Method-1
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = sorted(set(arr))[-2]
    print(result)

#Method-2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = sorted(set(arr), reverse=True)[1]
    print(result)

#Method-3
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newset = set(arr)
    newlist = list(newset)
    newlist.sort()
    print(newlist[-2])

#Method-4
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    lst.sort()
    print(lst[-2])

#Method-5
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))

#Method-6
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    lst.remove(max(lst))
    print(max(lst))
