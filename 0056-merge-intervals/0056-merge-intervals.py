class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # using  custom sort

        
        intervals.sort(key= lambda x : x[0])
        print(intervals)
        res = []
        
        for i in intervals:
            
            if not res or res[-1][1] < i[0]:
                res.append(i)

            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res