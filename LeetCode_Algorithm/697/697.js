var findShortestSubArray = function(nums) {
  // sol 
  var left = {}
  var right = {}
  var count = {}
  // enteries는 배열의 인덱스, value 쌍을 반환한다.
  for (const [idx, value] of nums.entries()){
    if (left[value] == undefined) {left[value] = idx}
    right[value] = idx
    if (count[value] ==undefined) {count[value] = 1}
    else{count[value] += 1}
  } 
  var ans = nums.length
  var arr = Object.keys(count).map((idx)=>{
    return count[idx]
  })

  // apply 메서드는 주어지는 this값과 배열로 제공되는 인자로 함수를 호출한다.
  var degree = Math.max.apply(null, arr)
  // 107ms 75%
  for (const key in count){
    if (degree == count[key]){
      let length = right[key] - left[key] + 1
      if (ans > length){
        ans = length
      }
    }
  }
  // 더 시간이 오래 걸리고 용량을 더 씀
  // 203ms 24%
  // Object.keys(count).map(key =>{
  //   console.log(count[key])
  //   if (degree == count[key]){
  //     let length = right[key]-left[key]+1
  //     if(ans > length){ans = length}
  //   }
  // })
  return ans


};

console.log(findShortestSubArray([1,2,2,3,1]))