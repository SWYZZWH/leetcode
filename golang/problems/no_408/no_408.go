package no_408

import "strconv"

func isDigit(i uint8) bool {
	return i <= '9' && i >= '0'
}

func validWordAbbreviation(word string, abbr string) bool {
	idx := 0
	for i := 0; i < len(abbr); i++ {
		if idx >= len(word) {
			return false
		}

		if isDigit(abbr[i]) {
			if abbr[i] == '0' {
				return false
			}
			num := 0
			if i == len(abbr)-1 || !isDigit(abbr[i+1]) {
				num, _ = strconv.Atoi(abbr[i : i+1])
			} else {
				if i != len(abbr)-2 && isDigit(abbr[i+2]) {
					return false
				}
				num, _ = strconv.Atoi(abbr[i : i+2])
				i++
			}
			idx += num
		} else {
			if word[idx] != abbr[i] {
				return false
			}
			idx++
		}
	}

	if idx != len(word) {
		return false
	}

	return true
}
