var hashMap = {
  '0' : '0',
  '1' : '1',
  '6' : '9',
  '8' : '8', 
  '9' : '6'
}
var dfs = function(str_idx) {
  if (2 * str_idx >= temp.length) {
    ans.push(temp.join(""))
    return 
  }
  for (let k in hashMap) {
    if (str_idx == 0 && k == '0') {
      continue
    }
    if (str_idx == parseInt(temp.length/2) && (k == '6' || k == '9')) {
      continue
    }
    temp[str_idx] = k
    temp[temp.length-1-str_idx] = hashMap[k]
    dfs(str_idx+1)
  }
}
var findStrobogrammatic = function(n) {
  // sol1 189ms 82% 62.4Mb 100%
  if (n == 1) {
    return ["0", "1", "8"]
  }
  temp = new Array(n).fill('0')
  ans = []
  dfs(0)
  return ans
};
console.log(findStrobogrammatic(3))