class Solution:
    def compress(self, chars: List[str]) -> int:
        # have an i going through and another pointer to show the insertion of the ch and counts
        # for evey new ch copy it
        # then go thorugh counting all occurances
        # insert the ch at the cur pointer
        # and for each digit in count insert at cur and increase cur

        i = 0
        cur  = 0
        while i < len(chars):
            # get character
            ch  = chars[i]
            count = 0
            # count all consecutive similar occurances
            while  i < len(chars) and chars[i] == ch:
                count+=1
                i+=1

            chars[cur] = ch
            cur +=1

            if count > 1:
                for digit in str(count):
                    chars[cur] = digit
                    cur+=1
        return cur
            

            
        
                