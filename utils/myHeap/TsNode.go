package myHeap

type TsNode struct {
	Ts  int
	Key int
	Val int
}

func (n TsNode) less(node Node) bool {
	newNode, ok := node.(*TsNode)
	if !ok {
		panic(any("wrong type"))
	}
	return n.Ts > newNode.Ts
}