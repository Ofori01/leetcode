// function removeDuplicates(nums) {
//     let currentNumber;
//     let offset;
//     nums.forEach(
//         (number, index)=>{
//             if (number !== currentNumber){
//                 currentNumber = number
//             }
//             else {
//                 nums.splice(index,1)
//                 offset++
//             }
//             console.log(currentNumber)
//             console.log(index)
//             console.log(nums) 
//         } 
//     )
//     return nums.length
// };

// removeDuplicates([1,1,1,2,2,2,3,3,4,5,5,6,6,6])
//would not work because access index is offset on every splice 
// Try for loop and manually update index and access 


// function removeDuplicates(nums : number []) : number {
//     let currentNumber;
//     let maxIndex = nums.length - 1;

//     for (let i = 0; i <= maxIndex;){
//         if(currentNumber !== nums[i]){
//             currentNumber = nums[i]
//             i++
//         }
//         else {
//             nums.splice(i,1); 
//             maxIndex--
//         }
//     }
//     return nums.length
// };


//This solution uses a pointer to track current unique number and iterates through the array
function removeDuplicates(nums) {

   let k= 0
   for(let i =0; i <nums.length;i++){
    if(nums[i]!==nums[k]){
        k++
        nums[k] = nums[i];
    }
   }
   return k
};
removeDuplicates([1,1,1,2,2,2,3,3,4,5,5,6,6,6])
