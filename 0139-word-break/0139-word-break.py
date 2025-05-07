class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # move r till valid, at next ch and move again. if all are valid. return true else return false if something is not valid

        # check = set(wordDict)
        # res = set()
        # cur_word = ''
        # for r in range(len(s)):
        #     cur_word+=s[r]
        #     print(cur_word)
        #     if cur_word in check:
        #         res.add(cur_word)
        #         cur_word = ''
        # if cur_word != '':
        #     res.add(cur_word)
        # print(res)
        # return all(word in check for word in res)

        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
                
        