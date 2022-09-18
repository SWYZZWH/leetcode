from typing import List

# dfs and remove duplication
#     void dfs(vector<vector<int>>& res, vector<int>& seq, vector<int>& nums, int pos) {
#         if(seq.size() > 1) res.push_back(seq);
#         unordered_set<int> hash;
#         for(int i = pos; i < nums.size(); ++i) {
#             if((seq.empty() || nums[i] >= seq.back()) && hash.find(nums[i]) == hash.end()) {
#                 seq.push_back(nums[i]);
#                 dfs(res, seq, nums, i + 1);
#                 seq.pop_back();
#                 hash.insert(nums[i]);
#             }
#         }
#     }

class Solution:
    # BFS
    # hash of tuple
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ret = []
        visited = set()
        for num in nums:
            cur_len = len(ret)
            for i in range(cur_len):
                if num >= ret[i][-1]:
                    new_tuple = ret[i] + (num,)
                    if new_tuple in visited:
                        continue
                    ret.append(new_tuple)
                    visited.add(new_tuple)
            if (num,) not in visited:
                ret.append((num,))
                visited.add((num,))

        return [arr for arr in ret if len(arr) > 1]