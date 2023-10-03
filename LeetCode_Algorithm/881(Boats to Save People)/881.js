var numRescueBoats = function(people, limit) {

  // sol1 155ms 85% 49.8MB 54%
  people.sort((a,b) => {return a-b})  
  let l = 0; let r = people.length-1; let ans = 0
  while (l <= r) {
    if (people[l] + people[r] <= limit) {
      l += 1; r -= 1
    } else {
      r -= 1
    }
    ans += 1
  }
  return ans
};
console.log(numRescueBoats([1,4,2,4], 5))