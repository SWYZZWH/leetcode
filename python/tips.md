### references

https://www.zhihu.com/people/one-seventh/posts
https://oi-wiki.org/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75924/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

### wait list
- kmp
- multiple dp
- scc
- amazon
    - https://www.1point3acres.com/bbs/thread-699232-1-1.html
    - https://www.1point3acres.com/bbs/thread-923632-1-1.html

### rolling hash

```python
from functools import reduce
from typing import List

MOD = 10 ** 9 + 7

def str2list(s: str) -> List[int]:
    return [ord(s[i]) - ord("a") for i in range(len(s))]

def cal_hash(nums: List[int], base: int) -> int:
    return reduce(lambda x, y: x * base + y, MOD)

# whether s2 in s1
def rabin_karp(s1: str, s2: str) -> bool:
    nums, nums2 = str2list(s1), str2list(s2)
    base = 26
    h = cal_hash(nums, base)
    h2 = cal_hash(nums2, base)
    base_l = pow(base, len(s2), MOD)
    for i in range(len(s2), len(nums)):
        h = h * base - nums[i - len(s2)] * base_l + nums[i]
        if h == h2:
          return True
    return False
```

### bit manipulation

```python
import numpy as np

a = 2
char_lst = list(np.binary_repr(a, a.bit_length()))
```

### sugar

```python
from string import ascii_lowercase

for c in ascii_lowercase:
    pass
```

```python
import functools
import itertools
import operator

for s in itertools.accumulate([1, 2, 3, 4, 5]):
    print(s)

a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
a = functools.reduce(operator.add, [1, 2, 3, 4, 5])
```

### array

1. two - sum / three - sum (arr[i] + arr[j] == k) * (two pointers / hashmap)
2. sorted array
3. subarray sum == k (arr[i] + ... + arr[j] == k) ** (prefix_sum)
4. subarray sum <= k (arr[i] + ... + arr[j] < k) *** (prefix_sum + binary search)
5. sum of left and smaller elements *** (merge sort)
6. sum of sub array with negative number * (one iteration, throw away left elements if cur_sum < 0)
7. sum of sub 2d matrix ** (sum rows i ... j, get an array, do question 6)
8. get any peak in array * (binary search)
9. 

### contiguous array sum

if we want to find the k continuous positive / negative / positive == negative number, just turn positive to 1, negative to - 1 and try to calculate the contiguous sum

### 字频压缩

```python
s = "abcdeabced"
freq = [0 for i in range(26)]
for c in s:
    freq[ord(c) - ord("a")] += 1
state = tuple(freq)  # now able to be hashed
```

### dp problems

tricks: append to the end of dp for border cases

stock: 3D dp array: day, max transactions, stocks currently hold in hand

0-1 pack: 2D dp: ith item, total weight

notice:

- for 0-1 backpack, outer loop: item, inner loop: weight

```python
def zero_one_knapsack():
    dp = [0 for i in range(budget + 1)]  # tips1: target + 1
    for i in range(0, len(present)):
        for j in reversed(range(present[i], budget + 1)):  # tips2: from back to front, and ignore 0 - present[i]          
            dp[j] = max(dp[j], dp[j - present[i]] + future[i] - present[i])
    return dp[-1]  # tips3: don't have to maintain a maximum
```

- for complete backpack, we need to rearrange the order of loop, may be even flip the inner loop and the outer loop
- top-down dp seems always get better performance in backpack problems

sequence problem:

#### top down dp

```python
class Solution:
    dp = {0: 0}

    def topDown(self, i):
        if i in self.dp:
            return self.dp[i]
        self.dp[i] = ...
```

### gcd

```python
def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)
```

### extend gcd (裴蜀定理)

equation: ax + by = c has the same solution with equation: a'x' + b'y' = c, a' = b and b' = a

cause b * x' + (a - b * (a // b)) * y' = c a * y' + b(1 - (a // b)) x' = c

so:
y' = x x' = y / (1 - (a // b))

at last, when b == 0 and return a == c, so at last x = 1, y = 0

we run basic gcd, get the return x, y of last gcd, calculate new x', y' recursively

### 波兰表达式

前缀 中缀 后缀 互转

mid -> suffix basic idea:

- num : output directly
- op: while op <= stk[-1], output stk[-1], then push op in stk
- ^, = : while op < stk[-1], output stk[-1], then push op in stk
- (: push directly in the stk
- ): pop all ops before until (
- EOF: pop all ops remaining in stk

#### log n:

```python
a = 1
n = a.bit_length()
# minimum larger than a:
2 ** n - 1
# maximum smaller than a:
2 ** (n - 1) - 1
```

#### set

literal set(tuple) is immutable declare like following to get a mutable set:

```python
t = set()
```

#### structure design

LRU: hashmap + double linked list

LFU:

#### Trie

```python
import collections


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.child = collections.defaultdict(TrieNode)

    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.isWord = True

    # usually doesn't need
    def searchWord(self, word):
        pass
```

#### Segement Tree

```python
# basic template
# https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
# https://oi-wiki.org/ds/seg/
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.d = [0 for i in range(4 * self.n)]
        self.build_tree(1, 0, self.n - 1)

    def build_tree(self, no: int, l: int, r: int):
        if l == r:
            self.d[no] = self.nums[l]
            return self.d[no]

        mid = (l + r) // 2
        self.d[no] = self.build_tree(2 * no, l, mid) + self.build_tree(2 * no + 1, mid + 1, r)
        return self.d[no]

    def update(self, index: int, val: int) -> None:
        # find all the way down 
        delta = val - self.nums[index]
        cur_no = 1
        self.d[cur_no] += delta
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if mid < index:
                cur_no = cur_no * 2 + 1
                l = mid + 1
            else:
                cur_no = cur_no * 2
                r = mid
            self.d[cur_no] += delta
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        cur_no = 1
        l, r = 0, self.n - 1

        def rec(no: int, l: int, r: int, left: int, right: int):
            if left <= l and r <= right:
                return self.d[no]

            ret = 0
            mid = (l + r) // 2
            if left <= mid:
                ret += rec(no * 2, l, mid, left, right)
            if right > mid:
                ret += rec(no * 2 + 1, mid + 1, r, left, right)
            return ret

        return rec(cur_no, l, r, left, right)

```

#### combination

next_permutation

Cnk

#### heap

1-indexed

for node i, left child is 2 * i, right child is 2 * i + 1 for node i, parent is i // 2

```python
import math

h = []


def swim(n):
    while n > 1 and h[n] < h[n // 2]:
        h[n], h[n // 2] = h[n // 2], h[n]
        n //= 2


def sink(n):
    if n >= len(h):
        return
    l = h[n * 2] if n * 2 <= len(h) else math.inf
    # r = h[n * 2 + 1] if n * 2 + 1<= len(h) else math.inf
    if h[n] <= l:
        return
    h[n], h[n * 2 + 1] = h[n * 2 + 1], h[n]
    sink(n * 2 + 1)
```

### Binary Search

![img_1.png](img_1.png)

idx range: range(0: len(arr) + 1)
bisect.bisect_left : find the left most element <= target bisect.bisect_right : find the first element on the right such as element > target

#### border case

when to use binary search:

- the answer is an integer or double, don't have to trace the solution
- 目的是要求出某個變數 "滿足某個條件" 的最小值，且變數超出此值後也都會繼續滿足此條件。
- 無法使用有效率的方法計算出答案，但只要給變數任意的值，都能容易的判斷出是否滿足條件。

template:

- when search for minimum
   ```python
    l, r = min, max  # max should be unacceptable or just 0 1000000
    while l < r:
      mid = (l + r) // 2
      success = check(mid) 
      if success: r = mid  # mid is okey and can be smaller
      else: l = mid + 1 # mid is not ok
    ```
- when search for maximum
   ```python
    l, r = min, max  # max should be unacceptable or just 0 1000000
    while l < r:
      mid = (l + r + 1) // 2 # notice !!
      success = check(mid) # ok with mid and larger
      if success: l = mid
      else: r = mid - 1 # mid is not okey
    ```

### classic graph algorithm

BFS should only be used in undirected graph as it can't find circle correctly in directed graph DFS visit graph always use coloring, but it is unnecessary as we can simply use a visited array + back
tracing

### virtual node

virtual head and tail in list questions

### monotonous queue / stack

monotonous stack:
Next/Last greatest/smallest element all elements smaller / greater than i, j

monotonous queue:
sliding window mainly solve problem about min/max of every subarray of fixed size “如果一个选手比你小还比你强，你就可以退役了。”——单调队列的原理

when it is possible to use monotonous queue / stack, it is also possible to use left / right min/max array

features:

- number goes up and down, and the relative relationship of neighbors matters
- when we visit i, the next sub problem only cares about the next and bigger index, or the next and smaller index, other indexes are useless
- one kind of pre-process
- information of original array is reduced
- time complexity is O(n)

Other:

- we can use sentinel to avoid popping from empty stack

template:

```python
class Solution:
    def monostoneStack(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                peek = stack.pop(-1)
                ans[peek] = i - peek
            stack.append(i)
        return ans
```

### 倍增

### 离散化

only work for float in python in python we can do like this:

```python
import heapq

floats = [1.0, 4.0, 3.5, 2.8]
h = []
for i, f in enumerate(floats):
    heapq.heappush(h, (f, i))
s = []
while h:
    p = heapq.heappop(h)
    s.append(p[1])
```

### ST table and RMQ

RMQ: range min/max query different from sum query: max(a, a) = a, max(a, b) = max(a, a) (b belongs to a)

### 树状数组

![img.png](pics/img.png)

#### bit manipulation

#### clear the least significant bit

n &= (n - 1)

#### keep the least significant bit

low_bit = x & -x

#### 自底向上更新

```python
# Python Version
def add(x, k):
    while x < n:  # 不能越界
        c[x] = c[x] + k
        x = x + lowbit(x)
```

#### 前缀和

```python
# Python Version
def getsum(x: int):  # sum(c[:x])
    ans = 0
    while x != 0:
        ans = ans + c[x]
        x = x - lowbit(x)
    return ans
```

#### 区间加

区间加指对区间 [i,j] 中所有元素值都增加 v 如果没有区间加的需求，不需要维护两个差分数组前缀和
![img.png](img.png)

```python
# t1 for sum(bi), t2 for sum(i * bi)
t1, t2, n = [0] * MAXN, [0] * MAXN, MAXN


def low_bit(x: int) -> int:
    return x & -x


def add(k: int, v: int):
    v1 = k * v
    while k <= n:
        t1[k] += v
        t2[k] += v1
        k += low_bit(k)


def add_range(l: int, r: int, v: int):
    add(l, v)
    add(r + 1, -v)


def get_sum(t, k):
    ret = 0
    while k != 0:
        ret += t[k]
        k -= low_bit(k)
    return ret


# prefix sum
def get_sum_range(l, r):
    return (r + 1) * get_sum(t1, r) - l * get_sum(t1, l - 1) -
    get_sum(t2, r) + get_sum(t2, l - 1)
```

### 线段树

#### build tree

```python
def build(nums, d, l, r, p):
    # zero-indexed
    if l == r:
        d[p] = nums[l]
        return
    m = (l + r) // 2
    build(nums, d, l, m, p * 2 + 1)
    build(nums, d, m + 1, r, p * 2 + 2)
    d[p] = d[p * 2 + 1] + d[(p * 2) + 2]


d = [0 for i in range(100)]
nums = []
build(nums, d, 0, 100, 0)
```

#### get range sum

```python
# Python Version
def getsum(l, r, s, t, p, d):
    # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号
    if l <= s and t <= r:
        return d[p]  # 当前区间为询问区间的子集时直接返回当前区间的和
    m = (l + r) // 2;
    sum = 0
    if l <= m:
        sum += getsum(l, r, s, m, p * 2 + 1, d)
    if r > m:
        sum += getsum(l, r, m + 1, t, p * 2 + 2, d)
    return sum
```

### range modify

```python

```

### 离散化

must get the whole array than deduplicate, sort and binary search the index

### how to solve range in leetcode

### merge list, sort, and split up into lists

```python
jobs = list(zip(startTime, endTime, profit))
jobs.sort(key=lambda x: x[0])
startTime, endTime, profit = list(zip(*jobs))
```

### sugar

```python
itertools.permutations([1,2,3]) # next_permutation in python 
collections.Counter(time)  # iterable, return a freq dict
collections.defaultdict(int)  # reference non-existed key return 0, not raise exception
```

### sortedcontainers:

sortedDict sortedList sortedSet can use bisect on keys:

```python
import sortedcontainers

s = sortedcontainers.SortedDict()

# insert: default descending order
s["a"] = 1
s["b"] = 2

# get: use index / get function

# pop(key) : get and remove

idx = s.bisect(key)  # return idx to insert, may be n, default is bisect_right
idx = s.bisect_left(key)  # if key is already in s.keys(), return the current idx of key, we should use bisect_left in most cases

# idx to key:
key = d.keys()[idx]

# get item by idx
d.peekitem(idx)
```

### get combination

````python
combinations(range(len(letter)), 2)
````

### sliding window

the size of range of each sub-problem is always fixed

### zip, zip longest

https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length

itertools.zip_longest(a, b, c)

### all

all for all element in a list meet the condition

### counting sort

when we meet constant size of input, like 0-9 a-z, we should consider use counting sort to optimize the time complexity

### KMP

most important point: shadow state

```python
    def strStr(self, haystack: str, needle: str) -> int:


m, n = len(haystack), len(needle)
nxt = [0 for i in range(n)]
shadow, cur = 0, 1
while cur < n:
    if needle[shadow] == needle[cur]:
        shadow += 1
        nxt[cur] = shadow
        cur += 1
    elif shadow == 0:
        cur += 1
    else:
        shadow = nxt[shadow - 1]

i, j = 0, 0
while i < m and j < n:
    if haystack[i] == needle[j]:
        i += 1
        j += 1
    elif j == 0:
        i += 1
    else:
        j = nxt[j - 1]

return i - m if j == n else -1 
```

```python
class Solution:
    # let's write down KMP
    def strStr(self, haystack: str, needle: str) -> int:
        M, N = len(haystack), len(needle)
        if N == 0:
            return 0

        # pre-computation
        next = [0 for i in range(N)]
        shadow, cur = 0, 1
        while cur < N:
            if needle[shadow] != needle[cur] and shadow != 0:
                shadow = next[shadow - 1]
            else:
                if needle[shadow] == needle[cur]:
                    shadow += 1
                next[cur] = shadow
                cur += 1

        i, j = 0, 0
        while i < M and j < N:
            if haystack[i] != needle[j] and j != 0:
                j = next[j - 1]
            else:
                if haystack[i] == needle[j]:
                    j += 1
                i += 1

        return i - N if j == N else -1

```

### Shortest Path

### Dijkstra Algorithm

### Cycle Detection

### Topological sort

the total number of node is given like N we can maintain an array incoming[N] and update

```python
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


cnt = [0 for i in range(numCourses)]
G = [set() for i in range(numCourses)]
for p in prerequisites:
    cnt[p[1]] += 1
    G[p[0]].add(p[1])

q = [i for i in range(numCourses) if cnt[i] == 0]
for idx in q:
    for j in G[idx]:
        cnt[j] -= 1
        if cnt[j] == 0:
            q.append(j)

return len(q) == numCourses
```

### MST(minimum spinning tree)

```python
    # Prim
def minimumCostPrim(self, N: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a, b, cost in connections:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    visited = set()
    cost = 0
    minHeap = [(0, 1)]
    while minHeap:
        minCost, city = heapq.heappop(minHeap)
        if city not in visited:
            cost += minCost
            visited.add(city)
            for nxt, c in graph[city]:
                if nxt not in visited:
                    heapq.heappush(minHeap, (c, nxt))
    return -1 if len(visited) < N else cost
```

### 0-1 BFS

### quick squaring

乘法且满足结合律

```c++
int qpow(int a, int n){
    int ans = 1;
    while(n){
        if(n&1)        //如果n的当前末位为1
            ans *= a;  //ans乘上当前的a
        a *= a;        //a自乘
        n >>= 1;       //n往右移一位
    }
    return ans;
}
```

### k hop minimum path

### LRU

double linked list + hash map double for find prev and delete easily it's better for implement a double linked list structure before implement LRU the interface of the double linked list should be:

```python
class DLinkedNode:

    def __init__(self, val: int = 0, prev: "DLinkedNode" = None, nxt: "DLinkedNode" = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __str__(self) -> str:
        return "val {}".format(self.val)


class DLinkedList:

    def __init__(self):
        self.head = DLinkedNode()
        self.tail = self.head

    def __len__(self) -> int:
        return 0

    def append(self, n: DLinkedNode):
        if n is None:
            return
        self.tail.nxt = n
        n.prev = self.tail
        self.tail = n

    def pop(self, n: DLinkedNode):
        prev = n.prev
        nxt = n.nxt
        prev.nxt = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev

    def popright(self):
        self.pop(self.tail)

    def popleft(self):
        n = self.head.nxt
        if not n:
            return
        self.pop(n)

    def __str__(self):
        cur = self.head.nxt
        i = 0
        ret = "List:\n"
        while cur is not None:
            ret += "\tnode {}: {}\n".format(i, cur)
            i += 1
            cur = cur.nxt

        return ret
```

map{key: Node}

### LFU

maintain a global min_freq maintain a freq map:{freq: NodeList} maintain a key map:{key: Node}