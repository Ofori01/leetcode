/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    

    function helper(left: number, right:number): void{

        // base case
        if(left >= right) return

        // general case
        [s[left], s[right]] = [s[right], s[left]]

        // recurrance relation
        helper(left+1, right-1)


    }

    helper(0, s.length -1)
};