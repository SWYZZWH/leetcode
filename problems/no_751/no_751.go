package no_751

import (
	"strconv"
	"strings"
)

//751. IP to CIDR

//An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character '.' splits the groups.
//
//For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) formatted as an IP address would be "15.136.255.107".
//A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length k. The addresses it covers are all the IPs whose first k bits are the same as the base IP address.
//
//For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20. Any IP address whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx, where x can be either 0 or 1, is in the set covered by the CIDR block.
//You are given a start IP address ip and the number of IP addresses we need to cover n. Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range [ip, ip + n - 1] exactly. No other IP addresses outside of the range should be covered.
//
//Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them.

// 7 <= ip.length <= 15
// ip is a valid IPv4 on the form "a.b.c.d" where a, b, c, and d are integers in the range [0, 255].
// 1 <= n <= 1000
// Every implied address ip + x (for x < n) will be a valid IPv4 address.

// try from start, increasing the prefix length gradually
// greedy strategy
func ipToCIDR(ip string, n int) []string {
	return rec(ipToInt(ip), ipToInt(ip)+(uint32(n)))
}

func rec(start uint32, end uint32) []string {
	n := end - start
	if n <= 0 {
		return nil
	}

	if n == 1 {
		return []string{strings.Join([]string{intToIp(start), "32"}, "/")}
	}

	// greedy
	base := findBase(int(n))
	mid := upper(start, base)
	mid2 := mid + uint32(pow(base))
	if mid2 > end {
		base = base - 1
		mid = upper(start, base)
		mid2 = mid + uint32(pow(base))
	}

	ret := []string{}
	ret = append(ret, rec(start, mid)...)

	ret = append(ret, strings.Join([]string{intToIp(mid), strconv.Itoa(32 - base)}, "/"))

	ret = append(ret, rec(mid2, end)...)
	return ret
}

func upper(x uint32, base int) uint32 {
	p := uint32(pow(base))
	if x%p == 0 {
		return x
	} else {
		return (x/p + 1) * p
	}
}

func pow(ex int) int {
	return 1 << ex
}

func addIp(ips []int, n int) []int {
	ret := make([]int, 0, 4)
	flag := n
	for i := len(ips) - 1; i >= 0; i-- {
		ret[i] = (ips[i] + flag) % 256
		flag = (ips[i] + flag) / 256
	}
	return ret
}

func ipToInt(ip string) uint32 {
	ret := uint32(0)
	for _, s := range strings.Split(ip, ".") {
		v, _ := strconv.Atoi(s)
		ret *= 256
		ret += uint32(v)
	}
	return ret
}

func intToIp(num uint32) string {
	ips := make([]string, 4)
	for i := 3; i >= 0; i-- {
		ips[i] = strconv.Itoa(int(num) % 256)
		num /= 256
	}
	return strings.Join(ips, ".")
}

func findBase(n int) int {
	ret := 0
	for n>>1 > 0 {
		n >>= 1
		ret++
	}
	return ret
}
