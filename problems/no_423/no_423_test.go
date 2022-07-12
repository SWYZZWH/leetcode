package no_423

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test423(t *testing.T) {
	require.Equal(t, "012", originalDigits("owoztneoer"))
	require.Equal(t, "45", originalDigits("fviefuro"))
	require.Equal(t, "", originalDigits(""))
	require.Equal(t, "0123456789", originalDigits("zeroonetwothreefourfivesixseveneightnine"))
	require.Equal(t, "000123456789", originalDigits("zeroonetwothreezerozerofourfivesixseveneightnine"))
}
