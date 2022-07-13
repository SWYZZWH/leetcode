package no_811

import (
	"strconv"
	"strings"
)

// 811. Subdomain Visit Count
//A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
//
//A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
//
//For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
//Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

type Node struct {
	self     string
	children map[string]*Node
	val      int
}

func subdomainVisits(cpdomains []string) []string {
	if cpdomains == nil || len(cpdomains) == 0 {
		return nil
	}
	// build root first
	root := Node{
		self:     "",
		children: map[string]*Node{},
		val:      0,
	}

	for _, countDomain := range cpdomains {
		countDomains := strings.Split(countDomain, " ")
		count, _ := strconv.Atoi(countDomains[0])
		domain := countDomains[1]
		domains := strings.Split(domain, ".")
		p := &root
		for i := len(domains) - 1; i >= 0; i-- {
			if node, ok := p.children[domains[i]]; ok {
				node.val += count
				p = node
			} else {
				newNode := &Node{
					domains[i],
					map[string]*Node{},
					count,
				}
				p.children[domains[i]] = newNode
				p = newNode
			}
		}
	}

	// DFS and print
	ret := make([]string, 0)
	visit(&root, "", &ret)
	return ret
}

func visit(root *Node, prefix string, ret *[]string) {
	if root == nil {
		return
	}
	domain := root.self
	if prefix != "" {
		domain = strings.Join([]string{domain, prefix}, ".")
	}
	if domain != "" {
		*ret = append(*ret, strings.Join([]string{strconv.Itoa(root.val), domain}, " "))
	}
	for _, node := range root.children {
		visit(node, domain, ret)
	}
}
