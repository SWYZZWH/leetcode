# 先排序，然后从后往前算，cnt[i] 表示该数为首位的情况下最多能向后拓展多少位连续的数字，初始 cnt[i] 都是 1, 最后返回 sum(cnt[i]) 就好了
# it is sub arrays that are asked!
# https://www.1point3acres.com/bbs/thread-920909-1-1.html