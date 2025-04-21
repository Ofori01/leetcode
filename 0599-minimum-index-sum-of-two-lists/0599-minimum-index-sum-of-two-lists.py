class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        check = {word: i for i,word in enumerate(list1)}
        res = []
        min_ = float('inf')

        for i,word in enumerate(list2):
            if word in check:
                if check[word] + i < min_:
                    min_ = check[word] + i
                    res = [word]
                elif check[word] + i == min_:
                    res.append(word)
        return res
