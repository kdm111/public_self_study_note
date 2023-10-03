var maximum69Number  = function(num) {
  // sol2 52ms 89% 42.4MB 15%
  let numArr = new Array(...String(num))
  for (let i = 0; i < numArr.length; i++) {
    if (numArr[i] == '6') {
      numArr[i] = '9'
      break
    }
  }
  return Number(numArr.join(""))
};
console.log(maximum69Number(6999))