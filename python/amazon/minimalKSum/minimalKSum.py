# 给了一个List, 和一个Int k。要你找出满足k - List.size( )个大小的最小缺失数字和。
# Example: [1, 3, 5, 7, 10] k = 7;
# Process: miss nums: 2, 4, 6, 8, 9;
# res: 我们需要 7 - 5 = 2 个缺失数字， 要想和最小，那就从头开始选，那就是2 + 4 = 6，
# 所以最后return 6
# from the head to the end, sum k numbers