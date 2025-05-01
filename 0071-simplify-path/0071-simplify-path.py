class Solution:
    def simplifyPath(self, path: str) -> str:
        p  = path.split('/')

        check = []

        for d in p:
            if d == ".." :
                if check:
                    check.pop()
            elif d != '.' and d!='':
                check.append(d)
        return '/'+ '/'.join(check)

        