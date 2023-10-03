var asteroidsDestroyed = function(mass, asteroids) {
  // sol2 220ms 29%  61.6MB 13.7%
  asteroids.sort((a,b) => {return a-b})
  for (let asteroid of asteroids) {
    if (mass < asteroid)
      return false
    mass += asteroid
  }
  return true
};

console.log(asteroidsDestroyed(10, [1,5,3]))