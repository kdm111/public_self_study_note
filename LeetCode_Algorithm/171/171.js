var titleToNumber = function(columnTitle) {
  // sol1 114~142ms 30~11%
  // right to left
  // var placeValue = 1
  // var ans = 0
  // for (let c of columnTitle.split("").reverse()){
  //   ans += placeValue * (c.charCodeAt() - 64)
  //   placeValue *= 26
  // }
  // return ans

  // sol2 102~127ms 47~19%
  // left to right
  var ans = 0
  var alphaMap = {}
  for (let i=65; i < 91; i++){
    alphaMap[String.fromCharCode(i)] = i-64
  }

  for (let c of columnTitle){
    ans = (ans * 26) + alphaMap[c]
  }
  return ans
};
console.log(titleToNumber("AB"))