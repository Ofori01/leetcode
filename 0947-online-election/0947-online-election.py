class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # actually about finding clossest time to use since times called may not be in the times list
        # create some form of list that at each time i list[i] tells who is leading
        self.times = times
        
        leaders= [0] * len(times)
        votes= defaultdict(int)
        cur_leader = float('-inf')
        max_votes = float('-inf')

        for i,time in enumerate(times):

            votes[persons[i]]+=1

            if votes[persons[i]] >= max_votes:

                cur_leader = persons[i]
                max_votes = votes[persons[i]]

            leaders[i] = cur_leader

        self.leaders = leaders
        print(leaders)


    def q(self, t: int) -> int:
        leaders = self.leaders
        # binary search time either the exact time or the time just less than t in our leaders. So basically last false
        times = self.times
        l, r = 0, len(times)

        while l < r :

            mid = (l+r) // 2

            if times[mid] <= t:
                l = mid + 1
            else:
                r = mid

        return leaders[l-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)