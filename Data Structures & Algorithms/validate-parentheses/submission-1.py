class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if c in hashmap: # if ), ], or }
                # check if the stack exists and top of stack == (, [, or {
                if stack and stack[-1] == hashmap[c]:
                    stack.pop() # if top of stack == (, [, or {, then pop
                else: # otherwise it's a mismatch so return false (eg. [})
                    return False
            else: # if c == (, [, or {, append to stack
                stack.append(c)

        # all items must be popped from stack (empty stack)
        if not stack: return True
        return False