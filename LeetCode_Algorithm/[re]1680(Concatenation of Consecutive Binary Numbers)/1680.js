var concatenatedBinary = function(n) {
  // sol3
  // 2^53-1을 넘는 값을 처리하지 못함
  // ans = ""; 

  // for (let i=1; i < n+1; i++) {
  //   ans += i.toString(2)
  // }
  // return parseInt(ans, 2) % (10**9+7)

  // sol4
  binary = []
  for (let num=1; num < n+1; num++) {
    temp = []
    while (num > 1) {
      temp.push(num & 1)
      num = num >> 1
    }
    if (num == 1){
      temp.push(1)
    }
    temp.reverse()
    binary = binary.concat(temp)
  }
  ans = 0; power = 0
  for (let i=binary.length-1; i >= 0; i--) {
    if (binary[i] == 1) {
      ans += 2 ** power
      ans = ans % (2**10+7)
    }
    power += 1
  }
  return ans
};

console.log(concatenatedBinary(3))
console.log(concatenatedBinary(42))
n = 2

console.log(n >> 1)
console.log(n >> 1)

