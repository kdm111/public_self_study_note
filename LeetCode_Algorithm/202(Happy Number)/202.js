var isHappy = function(n) {
  // sol1 O(n), O(n) 115~127ms 25~15%
  // var arr = new Array()
  // while (true) {

  //   let totalSum = 0
  //   while (n > 0 && n != undefined){
  //     remainder = n % 10
  //     n = parseInt(n / 10)
  //     totalSum += remainder ** 2
  //   }
  //   n = totalSum

  //   if (n == 1) { return true }

  //   if (arr.indexOf(n) < 0){ arr.push(n) }
  //   else { return false }
  // }

  // sol2 O(logn),O(1) 
  // floyd cycle detection algorithm
  // 68~103ms 90~38%

  let slow = n
  let fast = getNext(n)

  while (slow != 1 && fast != 1 && slow != fast){
    slow = getNext(slow)
    fast = getNext(getNext(fast))
  }
  return slow == 1 || fast == 1

};
var getNext= function(n) {
  var totalSum = 0
  while (n > 0){
    let remainder = n % 10
    n = parseInt(n/10)
    totalSum += remainder ** 2
  }
  return totalSum
}

console.log(isHappy(19))