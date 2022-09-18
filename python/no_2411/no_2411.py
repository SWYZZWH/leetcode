class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_idx = [0 for i in range(n + 1)]
        suffix_cnt = [[0 for j in range(32)] for i in range(n + 1)]

        def to_bit(num) -> List[int]:
            ret = [0 for i in range(32)]
            i = 0
            while num:
                ret[i] += num % 2
                num >>= 1
                i += 1
            return ret

        def add_num(cnt, num):
            lst = to_bit(num)
            # print(cnt, lst)
            for i in range(32):
                cnt[i] += lst[i]

        def remove_num(cnt, num):
            lst = to_bit(num)
            for i in range(32):
                cnt[i] -= lst[i]

        def contains_num(cnt, num) -> bool:
            lst = to_bit(num)
            for i in range(32):
                if lst[i] == 0:
                    continue
                if cnt[i] <= lst[i]:
                    return False

            return True

        i = n - 1
        while i >= 0:
            suffix_cnt[i] = suffix_cnt[i + 1]
            add_num(suffix_cnt[i], nums[i])
            r = suffix_idx[i + 1] + i
            while r > i and contains_num(suffix_cnt[i], nums[r]):
                remove_num(suffix_cnt[i], nums[r])
                r -= 1
            suffix_idx[i] = r - i + 1
            i -= 1

        return suffix_idx[:n]