
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([(i, ticket) for i, ticket in enumerate(tickets)])
        res = 0
        while q:
            i, ticket = q.popleft()
            ticket-=1
            res+=1
            if ticket == 0:
                if i == k:
                    return res
            else:
                q.append((i,ticket))
