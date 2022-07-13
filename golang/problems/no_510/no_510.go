package no_510

// 510. Inorder Successor in BST II
//Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.
//
//The successor of a node is the node with the smallest key greater than node.val.
//
//You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:
//
//class Node {
//    public int val;
//    public Node left;
//    public Node right;
//    public Node parent;
//}

type Node struct {
	Val    int
	Left   *Node
	Right  *Node
	Parent *Node
}

func inorderSuccessor(node *Node) *Node {
	if node == nil {
		return nil
	}

	if node.Right != nil {
		p := node.Right
		for p.Left != nil{
			p = p.Left
		}
		return p
	} else {
		p := node.Parent
		if p == nil {
			return nil
		}
		for p != nil && node == p.Right {
			node = p
			p = p.Parent
		}
		return p
	}
}
