var diagonalPrime = function(nums) {
  // sol1 81ms 82% 50MB 47%
  let i = 0; let j = nums[0].length -1; let ans = 0
  while (i < nums[0].length) {
    ans = Math.max(ans, isPrime(nums[i][i]), isPrime(nums[j][i]))
    i += 1; j -= 1
  }  
  return ans
};

var isPrime = function(n) {
  let i = 2;
  while (i * i <= n) {
    if (n % i == 0) 
      return -1
    i += 1
  }
  return n >= 2 ? n : -1
}

const prom = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(1)
    }, 1000)
  })
}
const add = (ret) => {
  return new Promise((resolve, _) => {
    setTimeout(() => {
      console.log(ret)
      resolve(ret+1)
    }, 1000)
  })
}
prom()
.then(add)
.then(add)
.then(add)