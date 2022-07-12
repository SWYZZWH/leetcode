package no_423

import "strings"

// 423. Reconstruct Original Digits from English
// Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

// :)
// notice:
// "zero"   // z count
// "two"	// w count
// "six"	// x count
// "seven"  // s count - 6 count
// "five"   // v count - 7 count
// "four"	// f count - 5 count
// "three"  // r count - 0 count - 4 count
// "eight"	// h count - 3 count
// "one"	// o count - 0 count - 2 cont - 4 count
// "nine"	// the rest is 9 count

func originalDigits(s string) string {
	freq := make(map[int32]int, 128)
	for _, c := range s {
		freq[c] += 1
	}

	zero := freq['z']
	two := freq['w']
	six := freq['x']
	seven := freq['s'] - six
	five := freq['v'] - seven
	four := freq['f'] - five
	three := freq['r'] - zero - four
	eight := freq['h'] - three
	one := freq['o'] - zero - two - four
	nine := (len(s) - 4*zero - 3*one - 3*two - 5*three - 4*four - 4*five - 3*six - 5*seven - 5*eight) / 4

	sb := strings.Builder{}
	sb.WriteString(strings.Repeat("0", zero))
	sb.WriteString(strings.Repeat("1", one))
	sb.WriteString(strings.Repeat("2", two))
	sb.WriteString(strings.Repeat("3", three))
	sb.WriteString(strings.Repeat("4", four))
	sb.WriteString(strings.Repeat("5", five))
	sb.WriteString(strings.Repeat("6", six))
	sb.WriteString(strings.Repeat("7", seven))
	sb.WriteString(strings.Repeat("8", eight))
	sb.WriteString(strings.Repeat("9", nine))
	return sb.String()
}
