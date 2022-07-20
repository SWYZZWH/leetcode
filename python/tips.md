#### top down dp
```python
class Solution:
    dp = {0: 0}
    def topDown(self, i):
        if i in self.dp:
            return self.dp[i]
        self.dp[i] = ...
```

#### log n:
```python
a = 1
n = a.bit_length()
# minimum larger than a:
2 ** n - 1
# maximum smaller than a:
2 ** (n - 1) - 1
```

