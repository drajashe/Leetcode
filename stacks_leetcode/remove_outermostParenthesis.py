''''1021. Remove Outermost Parentheses
Easy

49

33

Favorite

Share
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.'''

def removeOuterParentheses( S):
        left = 0
        right = 0
        result = ""
        start = 0
        for indx,char in enumerate(S):
            if char == "(":
                left += 1
            else:
                right += 1
            if right == left:
                result += S[start+1:indx]
                start = indx + 1
                right = 0
                left = 0

        return result

m="(()()())((()))"

S1=removeOuterParentheses(m)
print(S1)


