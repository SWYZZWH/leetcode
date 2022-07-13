package no_13

var mapping = map[string]int{
	"I":  1,
	"V":  5,
	"X":  10,
	"L":  50,
	"C":  100,
	"D":  500,
	"M":  1000,
	"IV": 4,
	"IX": 9,
	"XL": 40,
	"XC": 90,
	"CD": 400,
	"CM": 900,
}

func romanToInt(s string) int {
	ret := 0
	for i := 0; i < len(s); i++ {
		if i+1 < len(s) {
			if val, ok := mapping[s[i:i+2]]; ok {
				ret += val
				i++
				continue
			}
		}
		ret += mapping[s[i:i+1]]
	}
	return ret
}
