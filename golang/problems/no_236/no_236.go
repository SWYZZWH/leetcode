package no_236

import (
	"awesomeProject/golang/utils/TreeNode"
)

// 236. Lowest Common Ancestor of a Binary Tree
// My solution is build an auxiliary tree of which node is always points to parent
// then find the parent list of p,q will be much easy
// Complexity O(n)
// however, the procedure of the struct building is unnecessary
// just call find(val) to find the node and contains parents in a stack or map will also do

// besides, recursive way can also do
// if p, q both in the left tree, lowestCommonAncestor(root.left, p, q) will return parent
// if p, q both in the right tree, lowestCommonAncestor(root.right, p, q) will return parent
// else if p in the left tree and q in the right tree, the parent will be root
// else return nil

//type TreeNode.TreeNode struct {
//	Val   int
//	Left  *TreeNode.TreeNode
//	Right *TreeNode.TreeNode
//}

type TreeNodeDual struct {
	Parent *TreeNodeDual
	Left   *TreeNodeDual
	Right  *TreeNodeDual
	Self   *TreeNode.TreeNode
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func lowestCommonAncestor(root, p, q *TreeNode.TreeNode) *TreeNode.TreeNode {
	if root == nil || p == nil || q == nil {
		return nil
	}
	dualRoot := TreeNodeDual{Parent: nil, Self: root}
	index := map[*TreeNode.TreeNode]*TreeNodeDual{}
	buildDual(&dualRoot, index)

	pDual, qDual := index[p], index[q]
	pParents, qParents := []*TreeNode.TreeNode{}, map[int]*TreeNode.TreeNode{}
	for ; pDual != nil; pDual = pDual.Parent {
		pParents = append(pParents, pDual.Self)
	}
	for ; qDual != nil; qDual = qDual.Parent {
		qParents[qDual.Self.Val] = qDual.Self
	}

	for _, p := range pParents {
		if parent, ok := qParents[p.Val]; ok {
			return parent
		}
	}
	return nil
}

func buildDual(node *TreeNodeDual, index map[*TreeNode.TreeNode]*TreeNodeDual) {
	if node == nil || node.Self == nil {
		return
	}
	index[node.Self] = node
	if node.Self.Left != nil {
		node.Left = &TreeNodeDual{
			Parent: node,
			Self:   node.Self.Left,
		}
		buildDual(node.Left, index)
	}
	if node.Self.Right != nil {
		node.Right = &TreeNodeDual{
			Parent: node,
			Self:   node.Self.Right,
		}
		buildDual(node.Right, index)
	}
}
