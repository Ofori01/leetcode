/**
 Do not return anything, modify nums1 in-place instead.
 */
 function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    nums1.splice(m, nums1.length - 1, ...nums2);
    nums1.sort(
        (a,b)=> a-b
            
    )
    
 };