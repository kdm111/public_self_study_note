

var twoSum = function(nums, target) {
    // javascript는 n^2으로 풀림
    // for (let i=0 ;i < nums.length;i++){
    //     for (let j=1; j< nums.length;j++){
    //         if(i!=j && nums[i]+nums[j] == target){
    //             return [i,j]
    //         }
    //     }
        
    // }
    hashTable = []
    for (let idx = 0; idx < nums.length;idx ++){
        let targetNums = target - nums[idx]
        if (hashTable.includes(targetNums)){
            return [idx, hashTable.indexOf(targetNums)]
        }
        hashTable[idx] = nums[idx]
    }

};

console.log(twoSum([1,2,3], 4))