var multiply = function(num1, num2) {
  // sol1 576ms 5%
  ans = new Array(num1.length + num2.length).fill(0)
  num1 = num1.split("").reverse()
  num2 = num2.split("").reverse()

  let carry = 0
  for (let [p1, n1] of num1.entries()){
    for (let [p2, n2] of num2.entries()) {
      let carry = ans[p1+p2]
      let temp = parseInt(n1) * parseInt(n2) + carry
      ans[p1+p2] = temp % 10
      ans[p1+p2+1] += parseInt(temp / 10)
    }
    console.log(ans)
  }
  if (carry >= 1) {
    ans.push(carry)
  }
  ans.reverse()
  while (ans.length >= 2 && ans[0] == 0) {
    ans = ans.slice(1, ans.length)
  }
  return ans.join("")
};



console.log(multiply("0", "1111"))