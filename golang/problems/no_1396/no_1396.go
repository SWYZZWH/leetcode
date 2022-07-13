package no_1396

// 1396. Design Underground System

// An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.
//
//Implement the UndergroundSystem class:
//
//void checkIn(int id, string stationName, int t)
//A customer with a card ID equal to id, checks in at the station stationName at time t.
//A customer can only be checked into one place at a time.
//void checkOut(int id, string stationName, int t)
//A customer with a card ID equal to id, checks out from the station stationName at time t.
//double getAverageTime(string startStation, string endStation)
//Returns the average time it takes to travel from startStation to endStation.
//The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
//The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
//There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
//You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

// events flow can't be like that: id:0, t:0, station:s0 checkin ; id: 0, t :1, station:s1 checkin, id: 0, t :2, station:s2 checkin,
type info struct {
	count int
	sum   int
}

type checkInInfo struct {
	stationName string
	t           int
}

type UndergroundSystem struct {
	events map[int]checkInInfo
	stats  map[string]map[string]*info
}

func Constructor() UndergroundSystem {
	return UndergroundSystem{
		events: map[int]checkInInfo{},
		stats:  map[string]map[string]*info{},
	}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.events[id] = checkInInfo{stationName: stationName, t: t}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	start := this.events[id]
	if endStations, ok := this.stats[stationName]; !ok {
		this.stats[start.stationName] = map[string]*info{stationName: {
			count: 1,
			sum:   t - start.t,
		}}
	} else {
		if endStation, ok := endStations[stationName]; !ok {
			endStations[stationName] = &info{
				count: 1,
				sum:   t - start.t,
			}
		} else {
			endStation.count += 1
			endStation.sum += t - start.t
		}
	}
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	i := this.stats[startStation][endStation]
	return float64(i.sum) / float64(i.count)
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
