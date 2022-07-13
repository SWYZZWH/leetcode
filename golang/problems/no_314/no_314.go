package no_314

import (
	"awesomeProject/golang/utils/TreeNode"
)

// Let each node has a 2D position (x, y)，x for level and y for column
//
//if the level position fo parent node is x, the left child will be x + 1 and the right child will be y + 1
//
//if the column position fo parent node is y, the left child will be y -1, and the right child will be y + 1
//
//use BFS is easier, only thing to do is decide the x, y for each node
//
//notice : getting the range of the col will avoid the unnecessary sorting

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

// Queue mock queue
type Queue struct {
	store []*TreeNode2D
}

func (q *Queue) Enqueue(val *TreeNode2D) {
	if q.store == nil {
		q.store = []*TreeNode2D{val}
		return
	}

	q.store = append(q.store, val)
}

func (q *Queue) Dequeue() (*TreeNode2D, bool) {
	if q.store == nil || len(q.store) == 0 {
		return nil, false
	}
	ret := q.store[0]
	q.store = q.store[1:]
	return ret, true
}

//
//func verticalOrder(root *TreeNode) [][]int {
//	if root == nil {
//		return nil
//	}
//
//	ret := [][]int{}
//	q := Queue{}
//	q.Enqueue(root)
//
//	for len(q.store) != 0 {
//		tmpQueue := Queue{}
//		vals := []int{}
//		for len(q.store) != 0 {
//			node, _ := q.Dequeue()
//			vals = append(vals, node.Val)
//			if node.Left != nil {
//				tmpQueue.Enqueue(node.Left)
//			}
//			if node.Right != nil {
//				tmpQueue.Enqueue(node.Right)
//			}
//		}
//		ret = append(ret, vals)
//		q = tmpQueue
//	}
//	return ret
//}

type TreeNode2D struct {
	col int
	//level int
	node *TreeNode.TreeNode
}

// still try bfs, the problem of dfs is nodes in above may not always be visited fist
func verticalOrder(root *TreeNode.TreeNode) [][]int {
	if root == nil {
		return nil
	}
	ret := [][]int{}
	p := TreeNode2D{node: root, col: 0}
	q := Queue{}
	q.Enqueue(&p)
	colIndexMap := map[int][]int{}
	colMax, colMin := 0, 0
	for len(q.store) != 0 {
		node, _ := q.Dequeue()
		// insert in colIndexMap
		if _, ok := colIndexMap[node.col]; ok {
			colIndexMap[node.col] = append(colIndexMap[node.col], node.node.Val)
		} else {
			colIndexMap[node.col] = []int{node.node.Val}
		}
		colMax = max(colMax, node.col)
		colMin = min(colMin, node.col)
		if node.node.Left != nil {
			q.Enqueue(&TreeNode2D{col: node.col - 1, node: node.node.Left})
		}
		if node.node.Right != nil {
			q.Enqueue(&TreeNode2D{col: node.col + 1, node: node.node.Right})
		}
	}

	for i := colMin; i <= colMax; i++ {
		if index, ok := colIndexMap[i]; index != nil && ok {
			ret = append(ret, index)
		}
	}

	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

//func visitChild(child *TreeNode, colIndexMap map[int][]int, col int, colMax, colMin *int) {
//	if child == nil {
//		return
//	}
//	*colMax = max(col, *colMax)
//	*colMin = min(col, *colMin)
//	if indexs, ok := colIndexMap[col]; !ok {
//		colIndexMap[col] = []int{child.Val}
//	}
//
//	if child.Left != nil {
//		visitChild(child.Left, colIndexMap, col-1, colMax, colMin)
//	}
//	if child.Right != nil {
//		visitChild(child.Right, colIndexMap, col+1, colMax, colMin)
//	}
//}
