# the key is replacing the 0 with 1
# use prefix_sum to record the number of 0s in subarrays
# use prefix_prod to record the total product of subarrays

class ProductOfNumbers:

    def __init__(self):
        self.zeros = [0]
        self.prefix_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.zeros.append(self.zeros[-1] + 1)
            self.prefix_prod.append(self.prefix_prod[-1])
        else:
            self.zeros.append(self.zeros[-1])
            self.prefix_prod.append(self.prefix_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.zeros) - 1
        if self.zeros[n - k] != self.zeros[-1]:
            return 0
        return self.prefix_prod[-1] // self.prefix_prod[n - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)