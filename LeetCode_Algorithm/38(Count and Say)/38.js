var countAndSay = function(n) {
  // sol1 71ms 85% 44MB 39%  
  if (n == 1) {
    return "1"
  }
  let ans = countAndSay(n-1)
  let temp = ""; let i = 0;
  while (i < ans.length) {
    let j = i+1;
    while (j < ans.length && ans[i] == ans[j])
      j += 1
    temp += String(j-i)
    temp += String(ans[i])
    i = j
  }  
  return temp
};

console.log(countAndSay(4))