package no_1152

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test1152(t *testing.T) {
	require.Equal(t, []string{"about", "about", "career"}, mostVisitedPattern(
		[]string{"joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary", "mary"},
		[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},
		[]string{"home", "about", "home", "home", "cart", "maps", "home", "home", "about", "about", "career"}))
	require.Equal(t, []string{"b", "b", "a"}, mostVisitedPattern(
		[]string{"joe", "joe", "joe", "mary", "mary", "mary", "mary"},
		[]int{1, 2, 3, 4, 5, 6, 7},
		[]string{"b", "b", "a", "b", "a", "b", "a"}))
	require.Equal(t, []string{"hibympufi", "hibympufi", "yljmntrclw"}, mostVisitedPattern([]string{"h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"},
		[]int{527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079, 317455832, 411747930},
		[]string{"hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "yljmntrclw", "hibympufi", "yljmntrclw"}))
	require.Equal(t, []string{"jsips", "jsips", "bxbldeqhz"}, mostVisitedPattern([]string{"c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"},
		[]int{192769792, 207063377, 333805625, 890700372, 64199933, 245678250, 69530300, 833864121, 527969074, 492534187, 49153037, 143138463, 163274379},
		[]string{"jsips", "zkamv", "osajva", "bxbldeqhz", "zkamv", "osajva", "zkamv", "osajva", "zkamv", "zkamv", "zkamv", "zkamv", "jsips"}))
}
