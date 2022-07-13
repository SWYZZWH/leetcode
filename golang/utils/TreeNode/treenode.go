package TreeNode

import (
	"awesomeProject/golang/utils/algorithms"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// FromList use -1 to represent null
func FromList(values []int) *TreeNode {
	if values == nil || len(values) == 0 || values[0] == -1 {
		return nil
	}

	root := TreeNode{Val: values[0]}
	q := []*TreeNode{&root}
	i := 1
	for len(q) != 0 && i < len(values) {
		newQueue := []*TreeNode{}
		for j := 0; j < len(q); j++ {
			if i < len(values) && values[i] != -1 {
				left := TreeNode{Val: values[i]}
				q[j].Left = &left
				newQueue = append(newQueue, &left)
			}
			i++
			if i < len(values) && values[i] != -1 {
				right := TreeNode{Val: values[i]}
				q[j].Right = &right
				newQueue = append(newQueue, &right)
			}
			i++
		}
		q = newQueue
	}
	return &root
}

type TreeNode2D struct {
	p Position
	n *TreeNode
}

type Position struct {
	level int
	col   int
}

// printTree print tree with n as root
func (n *TreeNode) printTree() {
	grid := map[Position][]*TreeNode2D{}
	q := []*TreeNode2D{{Position{0, 0}, n}}
	levelMax, colMin, colMax := 0, 0, 0
	for len(q) != 0 {
		tmp := []*TreeNode2D{}
		for i := 0; i < len(q); i++ {
			colMax = algorithms.Max(colMax, q[i].p.col)
			colMin = algorithms.Min(colMin, q[i].p.col)
			if grid[q[i].p] == nil {
				grid[q[i].p] = []*TreeNode2D{q[i]}
			} else {
				grid[q[i].p] = append(grid[q[i].p], q[i])
			}

			if q[i].n.Left != nil {
				tmp = append(tmp, &TreeNode2D{Position{q[i].p.level + 1, q[i].p.col - 1}, q[i].n.Left})
			}
			if q[i].n.Right != nil {
				tmp = append(tmp, &TreeNode2D{Position{q[i].p.level + 1, q[i].p.col + 1}, q[i].n.Right})
			}
		}
		q = tmp
		levelMax++
	}
	for i := 0; i < levelMax; i++ {
		for j := colMin; j <= colMax; j++ {
			if n, ok := grid[Position{i, j}]; ok && n != nil {
				print("   ")
				for _, d := range n {
					print(" ")
					print(d.n.Val)
				}
			} else {
				print("\t")
			}
		}
		println()
	}
}
