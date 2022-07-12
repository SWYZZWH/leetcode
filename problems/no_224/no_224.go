package no_224

import "strconv"

// 224. Basic Calculator
//Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
//
//Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

// Constraints:
//
//1 <= s.length <= 3 * 105
//s consists of digits, '+', '-', '(', ')', and ' '.
//s represents a valid expression.
//'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
//'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
//There will be no two consecutive operators in the input.
//Every number and running calculation will fit in a signed 32-bit integer.

// s is always valid
// ' ' should always be ignored
//	'(' and ')' are always in pairs, expr = ( expr )
//  '+' expr = expr + expr
// '-' expr = - expr; expr = expr - expr
// expr = [0-9]*

// build a stack
type exprInfo struct {
	val   int
	class int
}

// when an expr was calculated, push in the stack
// check the top of the stack, cases are:
// 1. + on the top, pop + and the expr ahead, calculate, push in the expr
// 2. - on the top, pop -, if there is an expr ahead, pop out too, calculate, push in the expr

// notice: if we rewrite "A - B - C" as "A + (-B) + (-C)", then the expression can be calculated easily
func calculate(s string) int {
	if len(s) == 0 {
		return 0
	}

	stk := []exprInfo{}

	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			continue
		} else if s[i] == '(' {
			// next will be an expr
			left := 1
			j := i + 1
			for left != 0 {
				if s[j] == ')' {
					left--
				} else if s[j] == '(' {
					left++
				}
				j++
			}
			stk = pushInExpr(stk, calculate(s[i+1:j-1]))
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
		} else if s[i] <= '9' && s[i] >= '0' {
			j := i
			for j < len(s) && s[j] <= '9' && s[j] >= '0' {
				j++
			}
			val, _ := strconv.Atoi(s[i:j])
			stk = pushInExpr(stk, val)
			i = j - 1
		}
	}
	return stk[0].val
}

func pushInExpr(stk []exprInfo, expr int) []exprInfo {
	if len(stk) == 0 {
		stk = append(stk, exprInfo{
			val:   expr,
			class: 0,
		})
		return stk
	}

	// class of last can't be zero
	if last := stk[len(stk)-1]; last.class == 1 {
		exprLeft := stk[len(stk)-2]
		val := exprLeft.val + expr
		stk = stk[:len(stk)-2]
		stk = append(stk, exprInfo{
			val:   val,
			class: 0,
		})
	} else if last.class == 2 && (len(stk) == 1 || stk[len(stk)-2].class != 0) {
		// uni operation -
		stk = stk[:len(stk)-1]
		stk = append(stk, exprInfo{
			val:   -expr,
			class: 0,
		})
	} else if last.class == 2 {
		// binary operation -
		exprLeft := stk[len(stk)-2]
		val := exprLeft.val - expr
		stk = stk[:len(stk)-2]
		stk = append(stk, exprInfo{
			val:   val,
			class: 0,
		})
	}
	return stk
}
