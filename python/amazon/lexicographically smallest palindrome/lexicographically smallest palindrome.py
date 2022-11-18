# 原来已经是palindrome的password，然后需要rearrange然后求出一个lexicographically smallest palindrome。比如'baab'会变成'abba'
# get the frequency map of s
# if len(s) is odd, ret = s[len(s) // 2] else ret == ""
# for c in range(a - z)
#    ret = c * freq[c]// 2 + ret + c * freq[c] // 2
# return ret