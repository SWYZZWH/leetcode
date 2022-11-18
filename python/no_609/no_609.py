# Follow Up
# BFS can be used for great concurrency. Also, seek time would be greatly reduced as the files are co-located. Where as DFS would be requiring a lock on root node, if you are simultaneous processing the contents.
#
# If the files are too large, its better to Navigate first to get a list of file paths and then process the hash-map.
#
# Check the sizes of the files, if they match we need further processing.
# Maintain a checksum for the similar sizes, hash functions like sha256(hashes hardly collide) can be used to calculate checksums.
# If we can read only, 1Kb at a time, we can still use checksum for the blocks and calculate till the point they differ.
# May be read 0.5 kb from file 1 and 0.5 kb from file2 to check if they differ.
#
# import hashlib
# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# m.hexdigest()
# '19197dc4d03829df858011c6c87600f994a858103bbc19005f20987aa19a97e2'
# Time Complexty:
#
# For navigating, the files O(n), where n is the total number of files.
# For, calculating the checksums in case of similar sizes, we could approximate this as O( c + xb), where b is the number of blocks required to read till the files being compared differ, x is the constant for per-block overhead, and c is the constant for initialization and finalization.
# Further O(n) time is required to loop over the hashmap(key = f(size, checksum till they branch)) and return the once having more than 1 file path.
# Shloud consider to read the whole file content byte to byte.

# Follow up questions:
#
# 1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
# In general, BFS will use more memory then DFS. However BFS can take advantage of the locality of files in inside directories, and therefore will probably be faster
#
# 2. If the file content is very large (GB level), how will you modify your solution?
# In a real life solution we will not hash the entire file content, since it's not practical. Instead we will first map all the files according to size. Files with different sizes are guaranteed to be different. We will than hash a small part of the files with equal sizes (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte
#
# 3. If you can only read the file by 1kb each time, how will you modify your solution?
# This won't change the solution. We can create the hash from the 1kb chunks, and then read the entire file if a full byte by byte comparison is required.
#
# What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
# Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size
#
# How to make sure the duplicated files you find are not false positive?
# We will use several filters to compare: File size, Hash and byte by byte comparisons.


# Follow up:

# Imagine you are given a real file system, how will you search files? DFS or BFS?
# If the file content is very large (GB level), how will you modify your solution? digest hash
# If you can only read the file by 1kb each time, how will you modify your solution? hash ring
# What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
# How to make sure the duplicated files you find are not false positive?
import collections
from typing import List


class Solution:
    # map:
    #   key is the content
    #   value is the path
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ret = []
        content_map = collections.defaultdict(list)

        for p in paths:
            files = p.split(" ")
            d = files[0]
            for f in files[1:]:
                idx = f.find("(")
                content = f[idx + 1: -1]
                content_map[content].append("/".join([d, f[:idx]]))

        for v in content_map.values():
            if len(v) > 1:
                ret.append(v)

        return ret


