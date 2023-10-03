var minimumAbsDifference = function(arr) {
  // sol1 232~253ms 45~32%
  
  // arr.sort(function(a,b){return a-b})
  // var diff = 100000000000
  // var ans = []
  
  // for (let idx=1; idx<arr.length; idx++) {
  //   if ((arr[idx]-arr[idx-1]) < diff) {    
  //     ans = [[arr[idx-1], arr[idx]]]
  //     diff = arr[idx]-arr[idx-1]
  //   }
  //   else if ((arr[idx]-arr[idx-1]) == diff) {
  //     ans.push( [arr[idx-1], arr[idx]] )
  //   }
  // }
  // return ans

  // sol2 186~232ms 78~45%
  var minNum = Math.min(...arr)
  if (minNum < 0) {minNum *= -1}
  
  for (let idx=0; idx<arr.length; idx++){
    arr[idx] += minNum
  }

  var counts = new Array(Math.max(...arr)+1).fill(0)
  for (const num of arr){
    counts[num] = 1
  }

  var ans = []
  var idxI = -1; var idxII = -1
  var diff = 100000000000000
  for(let idx=0; idx<counts.length; idx++){
    if (counts[idx] == 1){
      idxI = idxII; idxII = idx
      if (idxI >= 0 && idxII >= 0) {
        var numI = idxI-minNum; var numII = idxII-minNum;
        if (numII-numI < diff){
          diff = numII-numI
          ans = [[numI, numII]]
        }
        else if (numII-numI == diff) {
          ans.push([numI, numII])
        }
      }
    }
  }
  return ans
  
  
};
console.log(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))