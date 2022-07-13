package no_811

import (
	"github.com/stretchr/testify/require"
	"sort"
	"testing"
)

func cmp(t *testing.T, src, expected []string) {
	sort.Strings(expected)
	result := subdomainVisits(src)
	sort.Strings(result)
	require.Equal(t, expected, result)
}

func Test811(t *testing.T) {
	cmp(t, []string{"1 google.mail.com", "1 google.mail.com"}, []string{"2 google.mail.com", "2 mail.com", "2 com"})
	cmp(t, []string{"9001 discuss.leetcode.com"}, []string{"9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"})
	cmp(t, []string{"900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"}, []string{"901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"})
}
