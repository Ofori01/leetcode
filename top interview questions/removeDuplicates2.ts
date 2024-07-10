function removeDuplicates(nums) {
    let k=0;
    let pairFound = false

    for(let i =1; i < nums.length; i++){
        if(nums[i] ===nums[k] && !pairFound){
            k++
            nums[k] = nums[i];
            pairFound = true
        }
        else if(nums[i] !==nums[k]){
            pairFound = false
            k++
            nums[k] = nums[i]
        }
        
    }
    
   return k+1
};

