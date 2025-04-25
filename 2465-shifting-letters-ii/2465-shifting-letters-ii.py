class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    #    compute cummulative changes array using -1 and 1
    # compute prefix sum of array and apply commulative sum to get res

        points = [0]* (len(s)+1)
        for start,end,shift in shifts:
            points[start] += -1 if shift == 0 else shift
            points[end+1] += 1 if shift == 0 else -shift
        cur  = 0
        for i,v in enumerate(points):
            cur += v
            points[i]= cur
        # print res
        res = ''

        for i,v in enumerate(points[:-1]):
            res+=chr( ((ord(s[i])-97+v)%26) + 97   )
        return res

        