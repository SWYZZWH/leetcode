package DSU

import "fmt"

type DisjointSetUnion struct {
	size    []int
	parents []int
}

func NewDSU(size int) DisjointSetUnion {
	if size < 0 {
		return DisjointSetUnion{}
	}
	dsu := DisjointSetUnion{parents: make([]int, size), size: make([]int, size)}
	for i := 0; i < size; i++ {
		dsu.parents[i] = i
		dsu.size[i] = 1
	}
	return dsu
}

func (d *DisjointSetUnion) IsRoot(child int) bool {
	return child == d.Find(child)
}

func (d *DisjointSetUnion) GetRootCnt() int {
	ret := 0
	for i, parent := range d.parents {
		if i == parent {
			ret += 1
		}
	}
	return ret
}

// Find the root of any node
// will the size/rank balanced optimization influence the find method? No
func (d *DisjointSetUnion) Find(child int) int {
	if child < 0 || child >= len(d.parents) {
		return -1
	}

	if p := d.parents[child]; p != child {
		d.parents[child] = d.Find(p)
		return d.parents[child]
	}

	return child
}

func (d *DisjointSetUnion) Union(child1, child2 int) bool {
	p1, p2 := d.Find(child1), d.Find(child2)
	if p1 == -1 || p2 == -1 {
		return false
	}
	if p1 == p2 {
		return true
	}
	if d.size[p1] < d.size[p2] {
		d.parents[p2] = p1
		d.size[p1] += d.size[p2]
	} else {
		d.parents[p1] = p2
		d.size[p2] += d.size[p1]
	}
	return true
}

func (d DisjointSetUnion) Show() {
	fmt.Println("DisjointSetUnion:")
	fmt.Printf("\tparents: %v\n", d.parents)
	fmt.Printf("\tsize: %v\n", d.size)
}
