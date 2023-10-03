var letterCombinations = function(digits) {
  // sol1 64ms 35% 41.8MB 77%
  if (digits == "")
    return []
  hashMap = {
    '2' : ['a','b','c'],
    '3' : ['d','e','f'],
    '4' : ['g','h','i'],
    '5' : ['j','k','l'],
    '6' : ['m','n','o'],
    '7' : ['p','q','r','s'],
    '8' : ['t','u','v'],
    '9' : ['w','x','y','z'],
  }
  digits = String(digits)
  ans = []
  backtracking(digits, 0, [])
  return ans
};

var backtracking = (digits, idx, str) => {
  if (digits.length == idx && str.length != 0) {
    ans.push(str.join("")); 
    return 
  }
  for (let c of hashMap[digits[idx]]) {
    str.push(c)
    backtracking(digits, idx+1, str)
    str.pop()
  }
}

console.log(letterCombinations())