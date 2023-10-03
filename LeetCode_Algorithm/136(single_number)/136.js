var singleNumber = function(nums) {
  // sol1 O(n), O(n) 76~89ms 84~68%
  // hashMap = new Map()
  // for (let num of nums){
  //   if (hashMap.has(num) == false){
  //     hashMap.set(num, 1)
  //   }else{
  //     hashMap.set(num, hashMap.get(num)+1)
  //   }
    
  // }
  // for (let key of hashMap.keys()){
  //   if (hashMap.get(key) == 1){
  //     return key
  //   }
  // }

  // sol2 O(n), O(n) 89~166ms 67~16%
  // totalSet = new Set(nums)
  // totalSet = Array.from(totalSet) // array.from => set to array
  // // totalSet = [...totalSet] // ES6 ...은 iterative한 객체를 하나씩 리턴한다.
  // // totalSetArray = new Array() // 배열로 변경한 뒤 다른 배열로 뽑아내어 복사
  // // Array.from(totalSet).forEach(function(elem, index, array){
  // //   totalSetArray.push(elem)
  // // })
  // // console.log(totalSetArray)
  // totalSetSum = totalSet.reduce((a,b)=>a+b, 0)
  // totalNumsSum = nums.reduce((a,b)=> a+b, 0)
  // return 2*totalSetSum - totalNumsSum

  // sol3 O(n), O(1) 71~104ms  89~49%
  // bit manipulation
  // num끼리 xor 연산을 한 뒤 그 수를 출력
  var ans = 0
  for (let num of nums){
    ans ^= num
    // num.toString(2) //2진수로 변환

  }
  return ans
  

}

console.log(singleNumber([1,2,4,2,1]))