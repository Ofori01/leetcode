class Solution:
    def romanToInt(self, s: str) -> int:

        numerals = {
            "I" : 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D":500,
            "M": 1000
        }

        diff = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        res = 0
        prev =''
        # normal conversion
        for i in s:
            if prev+ i  in diff:
                res= res -  numerals[prev] + diff[prev+i]
                prev= i
                
            else:
                res+= numerals[i]
                prev = i
        

        return res

        