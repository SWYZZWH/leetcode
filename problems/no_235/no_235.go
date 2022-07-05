package no_235

import "awesomeProject/utils/TreeNode"

// root is a BST, much simple, searchMap can be done in log(n)
// recursive method may be better
//
//func searchMap(root, p *TreeNode.TreeNode) map[int]*TreeNode.TreeNode {
//	ret := map[int]*TreeNode.TreeNode{}
//	if root == nil || p == nil {
//		return ret
//	}
//
//	for pp := root; pp != nil; {
//		ret[pp.Val] = pp
//		if pp.Val == p.Val {
//			return ret
//		}
//		if p.Val > pp.Val {
//			pp = pp.Right
//		} else {
//			pp = pp.Left
//		}
//	}
//
//	return ret
//}
//
//func searchLst(root, p *TreeNode.TreeNode) []*TreeNode.TreeNode {
//	ret := []*TreeNode.TreeNode{}
//	if root == nil || p == nil {
//		return ret
//	}
//
//	for pp := root; pp != nil; {
//		ret = append(ret, pp)
//		if pp.Val == p.Val {
//			return ret
//		}
//		if p.Val > pp.Val {
//			pp = pp.Right
//		} else {
//			pp = pp.Left
//		}
//	}
//
//	return ret
//}
//
//func lowestCommonAncestor(root, p, q *TreeNode.TreeNode) *TreeNode.TreeNode {
//	if root == nil || p == nil || q == nil {
//		return nil
//	}
//	parentsMap := searchMap(root, p)
//	parentsLst := searchLst(root, q)
//
//	for i := len(parentsLst) - 1; i >= 0; i-- {
//		if parent, ok := parentsMap[parentsLst[i].Val]; ok {
//			return parent
//		}
//	}
//
//	return nil
//}

func lowestCommonAncestor(root, p, q *TreeNode.TreeNode) *TreeNode.TreeNode {
	if root == nil || p == nil || q == nil {
		return nil
	}

	// 3 * 3 cases
	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestor(root.Left, p, q)
	} else if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	} else if p.Val >= root.Val && q.Val <= root.Val || p.Val <= root.Val && q.Val >= root.Val {
		return root
	}
	
	return nil
}
