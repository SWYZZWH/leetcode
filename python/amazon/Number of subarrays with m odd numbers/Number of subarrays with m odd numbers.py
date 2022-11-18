# Number of subarrays with m odd numbers


def countSubarrays(a, n, m):
    count = 0
    prefix = [0] * (n + 1)
    odd = 0

    # traverse in the array
    for i in range(n):
        prefix[odd] += 1

        # if array element is odd
        if (a[i] & 1):
            odd += 1

        # when number of odd elements>=M
        if (odd >= m):
            count += prefix[odd - m]

    return count


if __name__ == "__main__":
    # Driver Code
    a = [2, 2, 5, 6, 9, 2, 11]
    n = len(a)
    m = 2

    print(countSubarrays(a, n, m))
