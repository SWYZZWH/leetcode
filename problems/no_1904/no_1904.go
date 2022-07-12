package no_1904

import (
	"strconv"
	"strings"
)

//1904. The Number of Full Rounds You Have Played
//You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round starts.
//
//For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh round starts at 01:30.
//You are given two strings loginTime and logoutTime where:
//
//loginTime is the time you will login to the game, and
//logoutTime is the time you will logout from the game.
//If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight and from midnight to logoutTime.
//
//Return the number of full chess rounds you have played in the tournament.
//
//Note: All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45.

// Constraints:
//
//loginTime and logoutTime are in the format hh:mm.
//00 <= hh <= 23
//00 <= mm <= 59
//loginTime and logoutTime are not equal.

func numberOfRounds(loginTime string, logoutTime string) int {
	startH, startM := parseTime(loginTime)
	endH, endM := parseTime(logoutTime)
	if equals(startH, startM, endH, endM) {
		return 0
	}
	if !less(startH, startM, endH, endM) {
		ret := numberOfRounds(loginTime, "23:59") + numberOfRounds("00:00", logoutTime)
		if less(startH, startM, 23, 46) {
			ret += 1
		}
		return ret
	} else {
		ret := endH*4 + lower(endM) - startH*4 - upper(startM)
		if ret < 0 {
			ret = 0
		}
		return ret
	}
}

func parseTime(t string) (int, int) {
	ts := strings.Split(t, ":")
	hh, _ := strconv.Atoi(ts[0])
	mm, _ := strconv.Atoi(ts[1])
	return hh, mm
}

func less(sH, sM, eH, eM int) bool {
	if sH < eH {
		return true
	} else if sH > eH {
		return false
	} else {
		if sM < eM {
			return true
		} else {
			return false
		}
	}
}

func equals(sH, sM, eH, eM int) bool {
	return sH == eH && sM == eM
}

func upper(m int) int {
	if m == 0 {
		return 0
	} else {
		return (m-1)/15 + 1
	}

}

func lower(m int) int {
	return m / 15
}
