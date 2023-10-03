var uniquePaths = function(m, n) {
  // sol1
  // var arr = []
  // for (let i = 0 ; i < m; i++) {
  //   arr[i] = new Array(n)
  // }

  // sol2 81ms 63%
  var arr = Array.from(Array(m), ()=>Array(n).fill(1))
  for (let r=1; r < arr.length; r++){
    for (let c=1; c < arr[0].length; c++) {
      arr[r][c] = arr[r-1][c] + arr[r][c-1]
    }
  }
  return arr[m-1][n-1]
};

console.log(uniquePaths(3,7))