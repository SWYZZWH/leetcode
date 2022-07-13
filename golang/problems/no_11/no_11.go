package no_11

//11. Container With Most Water
//You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
//
//Find two lines that together with the x-axis form a container, such that the container contains the most water.
//
//Return the maximum amount of water a container can store.
//
//Notice that you may not slant the container.

// double pointer
// left and right
// if left > right, move right
// if right > left, move left
func maxArea(height []int) int {
	if height == nil || len(height) == 0 {
		return 0
	}

	i, j := 0, len(height)-1
	leftMax, rightMax := height[i], height[j]
	curArea := min(leftMax, rightMax) * (j - i)
	for i < j {
		if height[i] < height[j] {
			for i < j && height[i] <= leftMax {
				i++
			}
			if i >= j {
				return curArea
			}
			leftMax = height[i]
		} else {
			for i < j && height[j] <= rightMax {
				j--
			}
			if i >= j {
				return curArea
			}
			rightMax = height[j]
		}
		curArea = max(curArea, min(leftMax, rightMax)*(j-i))
	}
	return curArea
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
