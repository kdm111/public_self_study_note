var numberOfWeakCharacters = function(properties) {
  // sol1 247ms 100% 80MB 76%
  let maxAttack = 0
  for (let [a,_] of properties) {
    maxAttack = Math.max(a, maxAttack)
  }
  let defense = Array(maxAttack + 2).fill(0)
  for (let [a,d] of properties) {
    defense[a] = Math.max(defense[a], d)
  }
  for (let i=maxAttack-1; i >= 0; i--) {
    defense[i] = Math.max(defense[i], defense[i+1])
  }
  let ans = 0
  for (let [a,d] of properties) {
    if (d < defense[a+1]) {
      ans += 1
    }
  }
  return ans
};
console.log(numberOfWeakCharacters([[0,0], [2,2], [3,3]]))