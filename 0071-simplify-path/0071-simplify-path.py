class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        stack = []
        for der in p:
            if der == '..':
                if stack:
                    stack.pop()
            elif der!= '' and der != '.':
                stack.append(der)
        return '/' + '/'.join(stack)