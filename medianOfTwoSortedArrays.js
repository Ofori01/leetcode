/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let A=[]; let B = []; let median = 0;
    nums1.length >= nums2.length? (A = nums1, B = nums2) : (A= nums2, B = nums1);
    let a= A.length;
    let b = B.length
    let l = 0; let r = a-1;
    const half = Math.floor((a + b)/2)
    
    
    while (median === 0){
        let m = Math.floor((l+r)/2);
        let j = half - m -1;
        if(B[j]<= A[m+1] && A[m] <= B[j+1]){
            if ((a+b)%2 ===0){
                median = (Math.max(B[j],A[m])+Math.min(B[j+1],A[m+1]))/2
                return median

            }
            else {
                median = Math.min(B[j+1], A[m+1]);
                return median;
            }
        }
        else if (!(B[j] <= A[m+1])) l = m +1;
        else r = m-1;

    }


    
    
};