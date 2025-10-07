/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    // base case: n=1

    if (n === 1) return true
    else if( n < 1) return false

    n = n/4
    return isPowerOfFour(n)
};