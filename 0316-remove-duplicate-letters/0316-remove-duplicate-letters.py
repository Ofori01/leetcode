class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # have a set for visited
        # store the last index of ch
        # if a ch is already visited skip
        # if ch is lesser than top of the stack and ch is not the last ch of its kind pop. because if ch will be seen again then we can pop then add again ensuring order else we add as it is

        visited = set()
        last = {ch: i for i,ch in enumerate(s)}
        stack = []

        for i,ch in enumerate(s):
            if ch in visited:
                continue
            
            while stack and ch < stack[-1] and i < last[stack[-1]]:
                visited.remove(stack.pop())
            
            visited.add(ch)
            stack.append(ch)
        return ''.join(stack)