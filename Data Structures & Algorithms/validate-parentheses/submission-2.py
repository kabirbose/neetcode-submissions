class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'{':'}', '[':']', '(':')'}
        stack = []
        
        for i in reversed(range(len(s))):
            curr = s[i]
            
            if curr in [')', ']', '}']:
                stack.append(curr)
            
            elif curr in ['(', '[', '{']:
                # checks for extra open brackets
                # checks if we have a open bracket in the string but the stack is empty or if the open bracket doesn't match the close bracket in the top of the stack
                if not stack or hashmap[curr] != stack[-1]:
                    return False
                else: stack.pop()
        
        # checks for extra close brackets
        return len(stack) == 0