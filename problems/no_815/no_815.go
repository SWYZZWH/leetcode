package no_815

// BFS search
// shortest path problem (the least bus route)

func numBusesToDestination(routes [][]int, source int, target int) int {
	if source == target {
		return 0
	}

	routeInfo := make([]map[int]bool, len(routes))
	for i := 0; i < len(routes); i++ {
		routeInfo[i] = make(map[int]bool)
		for j := 0; j < len(routes[i]); j++ {
			routeInfo[i][routes[i][j]] = true
		}
	}

	routeSet := map[int]bool{}
	stopQueue := []int{}
	for i := 0; i < len(routeInfo); i++ {
		if routeInfo[i][source] {
			routeSet[i] = true
			stopSet := map[int]bool{}
			for j := 0; j < len(routes[i]); j++ {
				stop := routes[i][j]
				if _, ok := stopSet[stop]; !ok {
					if stop == target {
						return 1
					}
					stopQueue = append(stopQueue, stop)
					stopSet[stop] = true
				}
			}
		}
	}

	skip := 2
	// go back is invalid
	for len(stopQueue) > 0 {
		stopSet := map[int]bool{}
		tmpQueue := []int{}
		for i := 0; i < len(stopQueue); i++ {
			for j := 0; j < len(routeInfo); j++ {
				if routeSet[j] {
					continue
				}
				// can reach
				if _, ok := routeInfo[j][stopQueue[i]]; ok {
					for k := 0; k < len(routes[j]); k++ {
						if _, ok := stopSet[routes[j][k]]; !ok {
							if routes[j][k] == target {
								return skip
							}
							tmpQueue = append(tmpQueue, routes[j][k])
							stopSet[routes[j][k]] = true
						}
					}
					routeSet[j] = true
				}
			}
		}
		stopQueue = tmpQueue
		skip++
	}

	return -1
}
