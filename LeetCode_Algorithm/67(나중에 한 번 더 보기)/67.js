var addBinary = function(a, b) {
  // sol1 시간초과
  // var a = parseInt(a,2)
  // var b = parseInt(b,2)
  // return Number(a+b).toString(2)

  // sol2 O(max(m,n)), O(max(m,n)) 67~114ms 89~25%
  // var length = Math.max(a.length, b.length)
  // var a = a.padStart(length, '0')
  // var b = b.padStart(length, '0')
  
  // var carry = 0
  // var ans = ""
  // for (let idx=a.length-1; idx >=0; idx--){
  //   if (a[idx] == "1"){carry += 1}
  //   if (b[idx] == "1"){carry += 1}
  //   if (carry % 2 == 1) {
  //     ans += "1"
  //   }else{
  //     ans += "0"
  //   }
  //   carry = parseInt(carry/2)
  // }
  // if (carry == 1){
  //   ans += "1"
  // }
  // return ans.split("").reverse().join("")


  // sol3 107~167ms 33~5%
  var length = Math.max(a.length, b.length)
  var a = a.padStart(length, "0")
  var b = b.padStart(length, "0")
  var ans = ""
  var carry = 0
  for (let idx=a.length-1; idx >= 0; idx--){
    numA = Number(a[idx]); numB = Number(b[idx])
    let digitSum = numA ^ numB ^ carry
    carry = (numA && numB) || (numB && carry) || (carry && numA)
    ans += String(digitSum)
  }
  if (carry == 1){ans += "1"}
  return ans.split("").reverse().join("")

};
console.log(addBinary("11", "1"))