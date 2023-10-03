var asteroidCollision = function(asteroids) {
  // sol1 O(n) O(n) 60ms 99%
  let ans = []
  for (let asteroid of asteroids) {
    let flag = true
    while (ans.length > 0 && asteroid < 0 && 0 < ans[ans.length-1]) {
      if (ans[ans.length-1] < -asteroid) {
        ans.pop(); 
        continue
      } else if (ans[ans.length-1] == -asteroid) {
        ans.pop(); flag = false
      } else {
        flag = false
      }
      break
    }
    if (flag == true) {
      ans.push(asteroid)
    }
  }
  return ans
};

console.log(asteroidCollision([5,10,-5]))