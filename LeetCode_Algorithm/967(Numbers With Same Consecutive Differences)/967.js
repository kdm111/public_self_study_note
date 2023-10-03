var check = function(n) {
  return (-1 < n && n < 10)
}
var solve = function(i, k, temp, n) {
  temp.push(i)
  if (temp.length == n) {
    ans.add(temp.join("")); 
    return ;
  }
  if (check(i-k)) {
    solve(i-k, k, temp, n); temp.pop()
  }
  if (check(i+k)) {
    solve(i+k, k, temp, n); temp.pop()
  }
}
var numsSameConsecDiff = function(n, k) {
  // sol1 111ms 50%
  ans = new Set()
  for (let i=1; i < 10; i++) {
    solve(i, k, [], n)
  }
  let ret = Array.from(ans, (num)=>{return parseInt(num)})
  return ret
};

console.log(numsSameConsecDiff(3,1))