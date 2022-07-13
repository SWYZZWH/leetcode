package no_227

import "strconv"

// 227. Basic Calculator II
// Given a string s which represents an expression, evaluate this expression and return its value.
//
//The integer division should truncate toward zero.
//
//You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
//
//Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

// Constraints:
//
//1 <= s.length <= 3 * 105
//s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
//s represents a valid expression.
//All the integers in the expression are non-negative integers in the range [0, 231 - 1].
//The answer is guaranteed to fit in a 32-bit integer.

// build a stack
type exprInfo struct {
	val   int
	class int
}

// '+', '-', '*', '/' are binary operators
// '/' returns integer
// ignore " "

// Approach 2: Optimised Approach without the stack
// turn 1 - 1 to 1 + (-1)
// if "1 + 2 * 3", we keep 1 until find next operator "*", then the 1 can be added to the sum
func calculate(s string) int {
	if len(s) == 0 {
		return 0
	}
	stk := make([]exprInfo, 0)
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			continue
		}
		if s[i] <= '9' && s[i] >= '0' {
			j := i
			for j < len(s) && s[j] <= '9' && s[j] >= '0' {
				j++
			}
			val, _ := strconv.Atoi(s[i:j])
			stk = pushInExpr(stk, val)
			i = j - 1
		} else if s[i] == '+' {
			stk = append(stk, exprInfo{
				val:   0,
				class: 1,
			})
		} else if s[i] == '-' {
			stk = append(stk, exprInfo{
				val:   0,
				class: 2,
			})
		} else if s[i] == '*' {
			stk = append(stk, exprInfo{
				val:   0,
				class: 3,
			})
		} else if s[i] == '/' {
			stk = append(stk, exprInfo{
				val:   0,
				class: 4,
			})
		}
	}
	return popAll(stk)
}

func popAll(stk []exprInfo) int {
	ret := stk[0].val
	for i := 1; i < len(stk)-1; i = i + 2 {
		if stk[i].class == 1 {
			ret += stk[i+1].val
		} else {
			ret -= stk[i+1].val
		}

	}
	return ret
}

func pushInExpr(stk []exprInfo, expr int) []exprInfo {
	if len(stk) == 0 {
		stk = append(stk, exprInfo{
			val:   expr,
			class: 0,
		})
		return stk
	}

	val := 0
	if symbol, exprLeft := stk[len(stk)-1], stk[len(stk)-2]; symbol.class == 3 {
		val = exprLeft.val * expr
	} else if symbol.class == 4 {
		val = exprLeft.val / expr
	} else {
		stk = append(stk, exprInfo{
			expr,
			0,
		})
		return stk
	}
	stk[len(stk)-2] = exprInfo{
		val:   val,
		class: 0,
	}
	return stk[:len(stk)-1]
}
