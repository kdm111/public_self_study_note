var addDigits = function(num) {
    
  // sol1 82~93ms 76~63%
  var num = String(num)
  while (num.length != 1) {
    let ans = 0
    for (let n of num){
      ans += parseInt(n)
    }
    num = String(ans)
  }
  return num

  // digital root
};

console.log(addDigits(38))