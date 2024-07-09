function removeElement(nums: number[], val: number): number {
    let j = nums.length - 1
    for(let i =0 ; i <= j; i++){
        if(nums[i] === val){
            while(nums[j] === val && i < j){
                j--
            } 
            nums[i] = nums[j];
            j--
        }
    }
    return j +1

};