package no_1762

//1762. Buildings With an Ocean View

//There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
//
//The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
//
//Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

func findBuildings(heights []int) []int {
	if heights == nil || len(heights) == 0 {
		return nil
	}

	ret := make([]int, len(heights))
	cur := len(heights) - 1
	heightest := 0
	for i := len(heights) - 1; i >= 0; i-- {
		if heights[i] > heightest {
			heightest = heights[i]
			ret[cur] = i
			cur--
		}
	}
	return ret[cur+1:]
}
