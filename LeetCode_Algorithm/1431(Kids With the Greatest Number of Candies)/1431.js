var kidsWithCandies = function(candies, extraCandies) {
  // sol1 63ms 57% 42.3MB 56%
  let maxCandy = Math.max(...candies)  
  for (let i=0; i < candies.length; i++) {
    if (candies[i] + extraCandies >= maxCandy) {
      candies[i] = true
    } else {
      candies[i] = false
    }
  }
  return candies
};