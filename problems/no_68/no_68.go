package no_68

import "strings"

// 68. Text Justification
// Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
//
// You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
//
// Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
//
// For the last line of text, it should be left-justified, and no extra space is inserted between words.

func fullJustify(words []string, maxWidth int) []string {
	lines := [][]string{{}}
	lineIdx := 0
	curLen := 0
	for i := 0; i < len(words); i++ {
		if curLen+len(words[i])+len(lines[lineIdx]) > maxWidth {
			lineIdx++
			newLine := []string{words[i]}
			lines = append(lines, newLine)
			curLen = len(words[i])
		} else {
			lines[lineIdx] = append(lines[lineIdx], words[i])
			curLen += len(words[i])
		}
	}

	return printLines(lines, maxWidth)
}

func printLines(lines [][]string, maxWidth int) []string {
	ret := make([]string, len(lines))
	for i := 0; i < len(lines); i++ {
		if i == len(lines)-1 {
			ret[i] = printLastLine(lines[i], maxWidth)
		} else {
			ret[i] = printNormalLine(lines[i], maxWidth)
		}
	}
	return ret
}

func printNormalLine(line []string, maxWidth int) string {
	if len(line) == 0 {
		return strings.Repeat(" ", maxWidth)
	}
	if len(line) == 1 {
		return strings.Join([]string{line[0], strings.Repeat(" ", maxWidth-len(line[0]))}, "")
	}
	wordLengthSum := 0
	sepCnt := len(line) - 1
	for i := 0; i < len(line); i++ {
		wordLengthSum += len(line[i])
	}
	spaceLenSum := maxWidth - wordLengthSum
	avg, res := spaceLenSum/sepCnt, spaceLenSum%sepCnt

	sb := strings.Builder{}
	for i := 0; i < len(line); i++ {
		if i != 0 {
			spaceCnt := avg
			if res > 0 {
				res--
				spaceCnt++
			}
			sb.WriteString(strings.Repeat(" ", spaceCnt))
		}
		sb.WriteString(line[i])
	}
	return sb.String()
}

func printLastLine(line []string, maxWidth int) string {
	sb := strings.Builder{}
	length := 0
	for i := 0; i < len(line); i++ {
		if i != 0 {
			sb.WriteString(" ")
			length += 1
		}
		sb.WriteString(line[i])
		length += len(line[i])
	}
	sb.WriteString(strings.Repeat(" ", maxWidth-length))
	return sb.String()
}
