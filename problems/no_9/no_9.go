package no_9

//9. Palindrome Number
//Given an integer x, return true if x is palindrome integer.
//
//An integer is a palindrome when it reads the same backward as forward.
//
//For example, 121 is a palindrome while 123 is not.

// -231 <= x <= 231 - 1
// we can use constant mem space
// without convert to string
// all palindrome problem can be done by :
// assert number reverted equals to the original one
func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	num := x
	reverted := 0
	for num > 0 {
		reverted *= 10
		reverted += num % 10
		num /= 10
	}

	return x == reverted
}
