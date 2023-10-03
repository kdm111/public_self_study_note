var fizzBuzz = function(n) {
  // sol1 O(n) 58~74ms 99~81%
  // ans = []
  // for (let num=1; num < n+1; num++){
  //   numAnsStr = ""
  //   if (num <= 2){
  //     num = String(num)
  //     ans.push(num)
  //     continue 
  //   }

  //   if ((num % 3 == 0) && (num % 5 == 0)){
  //     numAnsStr = "FizzBuzz"
  //   }
  //   else if (num % 3 == 0){
  //     numAnsStr = "Fizz"
  //   }
  //   else if (num % 5 == 0 ){
  //     numAnsStr = "Buzz"
  //   }
  //   else {
  //     numAnsStr = String(num)
  //   }
  //   ans.push(numAnsStr)
  // }
  // return ans

  // sol2 95~114ms 53~27%보다 빠름
  ans = []
  hashMap = {
    3 : "Fizz",
    5 : "Buzz"
  }
  for (let num=1; num < n+1; num++){
    ansNumStr = ""
    for (let key in hashMap){
      if (num % key == 0){
        ansNumStr += hashMap[key]
      }
    }
    if (ansNumStr==""){
      ansNumStr = String(num)
    }
    ans.push(ansNumStr)
  }
  return ans

};

console.log(fizzBuzz(15))