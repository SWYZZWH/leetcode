package no_1650

// just a simple version of 236
// same solution

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Parent *Node
}

func lowestCommonAncestor(p, q *Node) *Node {
	if p == nil || q == nil {
		return nil
	}

	qParents := map[int]*Node{}
	for qq := q; qq != nil; qq = qq.Parent {
		qParents[qq.Val] = qq
	}

	for pp := p; pp != nil; pp = pp.Parent {
		if parent, ok := qParents[pp.Val]; ok {
			return parent
		}
	}
	return nil
}
