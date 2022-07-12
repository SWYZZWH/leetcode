package no_394

import (
	"strconv"
	"strings"
)

// 394. Decode String

// Given an encoded string, return its decoded string.
//
//The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
//
//You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
//
//The test cases are generated so that the length of the output will never exceed 105.

// more efficient way may use stack
func decodeString(s string) string {
	sb := strings.Builder{}
	for i := 0; i < len(s); {
		if isDigit(s[i]) {
			num, j := parseNum(s, i)
			end := parseBracket(s, j)
			sb.WriteString(strings.Repeat(decodeString(s[j+1:end]), num))
			i = end + 1
		} else if s[i] == '[' {
			end := parseBracket(s, i)
			sb.WriteString(strings.Repeat(decodeString(s[i+1:end]), 1))
			i = end + 1
		} else if isAlpha(s[i]) {
			end := i
			for end < len(s) && isAlpha(s[end]) {
				end++
			}
			sb.WriteString(s[i:end])
			i = end
		}
	}
	return sb.String()
}
func isDigit(c uint8) bool {
	return c <= '9' && c >= '0'
}

func isAlpha(c uint8) bool {
	return c <= 'z' && c >= 'a'
}

func parseNum(s string, start int) (int, int) {
	i := start
	for i < len(s) && isDigit(s[i]) {
		i++
	}
	num, _ := strconv.Atoi(s[start:i])
	return num, i
}

func parseBracket(s string, start int) int {
	// start is left bracket
	i := start
	level := 0
	for i < len(s) {
		if s[i] == '[' {
			level++
		} else if s[i] == ']' {
			level--
		}

		if level == 0 {
			return i
		}
		i++
	}
	return -1
}
