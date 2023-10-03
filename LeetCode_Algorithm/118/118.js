var generate = function(numRows) {
  // sol1 77~81ms 59~52%
  var ans = []
  for (let numRow=1; numRow < numRows+1; numRow++){
    let temp = []
    for (let i=0; i < numRow; i++){
      temp.push(null)
    }
    temp[0] = 1; temp[temp.length-1] = 1
    if (temp.length == 1){
      ans.push(temp); continue
    }
    
    last = ans[ans.length-1]
    for (let j=0; j < last.length-1; j++){
      let k = last[j]+last[j+1]
      temp[j+1] = k
    }
    ans.push(temp)

  }
  return ans
};

console.log(generate(6))

