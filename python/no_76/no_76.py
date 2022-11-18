import collections


# class Solution:
#     # sliding window:
#     #   if the condition is not met, r ++
#     #   else shrink the left borad until the condition is not met
#     # the most difficult part is how to reduce the time complexity of check the condition to O(1)
#     # this problem shows we can consider to use just one number, but not a complicated data structure
#
#     # border condition is trivial
#     def minWindow(self, s: str, t: str) -> str:
#         c = collections.Counter(t)
#         conditions = len(c.keys())
#
#         i, j = -1, -1
#         ret_i, ret_j = -1, -1
#         cur_condition = 0
#         cur_d = collections.defaultdict(int)
#         ret = len(s)
#         while j != len(s):
#             # try move j
#             while cur_condition != conditions:
#                 j += 1
#                 if j == len(s):
#                     break
#                 if s[j] not in c:
#                     continue
#                 cur_d[s[j]] += 1
#                 if cur_d[s[j]] == c[s[j]]:
#                     cur_condition += 1
#
#             # try move i
#             while cur_condition == conditions:
#                 i += 1
#                 if s[i] not in c:
#                     continue
#                 if cur_d[s[i]] == c[s[i]]:
#                     if j - i + 1 <= ret:
#                         ret_i = i
#                         ret_j = j + 1
#                         ret = min(ret, ret_j - ret_i)
#                     cur_condition -= 1
#                 cur_d[s[i]] -= 1
#
#         return s[ret_i: ret_j]


class Solution:
    # sliding window:
    #   if the condition is not met, r ++
    #   else shrink the left borad until the condition is not met
    # the most difficult part is how to reduce the time complexity of check the condition to O(1)
    # this problem shows we can consider to use just one number, but not a complicated data structure
    def minWindow(self, s: str, t: str) -> str:
        c = collections.Counter(t)
        cur_condition = 0
        i = 0
        ret = ""
        # standard template of sliding window
        for j in range(len(s)):
            if s[j] not in c:
                continue
            c[s[j]] -= 1
            if c[s[j]] == 0:
                cur_condition += 1
            while cur_condition == len(c.keys()):
                if j - i < len(ret) or ret == "":
                    ret = s[i: j + 1]
                if s[i] in c:
                    c[s[i]] += 1
                if c[s[i]] > 0:
                    cur_condition -= 1
                i += 1

        return ret
