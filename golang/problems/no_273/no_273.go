package no_273

import "strings"

// 273. Integer to English Words
// Convert a non-negative integer num to its English words representation.

func numberToWords(num int) string {
	numWord := map[int]string{
		0:          "Zero",
		1:          "One",
		2:          "Two",
		3:          "Three",
		4:          "Four",
		5:          "Five",
		6:          "Six",
		7:          "Seven",
		8:          "Eight",
		9:          "Nine",
		10:         "Ten",
		11:         "Eleven",
		12:         "Twelve",
		13:         "Thirteen",
		14:         "Fourteen",
		15:         "Fifteen",
		16:         "Sixteen",
		17:         "Seventeen",
		18:         "Eighteen",
		19:         "Nineteen",
		20:         "Twenty",
		30:         "Thirty",
		40:         "Forty",
		50:         "Fifty",
		60:         "Sixty",
		70:         "Seventy",
		80:         "Eighty",
		90:         "Ninety",
		100:        "Hundred",
		1000:       "Thousand",
		1000000:    "Million",
		1000000000: "Billion",
	}

	if num == 0 {
		return numWord[num]
	}

	words := []string{}
	if b := num / 1000_000_000; b != 0 {
		words = append(words, strings.Join([]string{numWord[b], numWord[1000000000]}, " "))
		num %= 1000_000_000
	}

	if m := num / 1000_000; m != 0 {
		words = append(words, strings.Join([]string{parseThousand(m, numWord), numWord[1000000]}, " "))
		num %= 1000_000
	}

	if t := num / 1000; t != 0 {
		words = append(words, strings.Join([]string{parseThousand(t, numWord), numWord[1000]}, " "))
		num %= 1000
	}

	if num != 0 {
		words = append(words, parseThousand(num, numWord))
	}
	return strings.Join(words, " ")
}

// m: [0, 1000)
func parseThousand(num int, numWord map[int]string) string {
	words := []string{}
	if h := num / 100; h != 0 {
		words = append(words, strings.Join([]string{numWord[h], numWord[100]}, " "))
		num %= 100
	}
	if num == 0 {
		return strings.Join(words, " ")
	}
	if num < 20 {
		words = append(words, numWord[num])
		return strings.Join(words, " ")
	}
	i := num % 10
	t := num - i
	if i != 0 {
		words = append(words, strings.Join([]string{numWord[t], numWord[i]}, " "))
	} else {
		words = append(words, numWord[t])
	}

	return strings.Join(words, " ")
}
