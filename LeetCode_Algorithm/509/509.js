
var fib = function(n) {
  // sol1 O(n), O(1) 92~104ms 51~47%보다 빠름
  // n이 1000일 경우 5ms
  // if (n <= 1){return n}
  // var first = 0
  // var second = 1
  // for (let i=2;i < n+1; i++){
  //   var third = first+second
  //   first = second 
  //   second = third
  // }
  // return third

  // sol2 O(2^n) 84~112ms 62~41%보다 빠름 
  // n이 40일 경우 945ms
  // if (n<=1) {return n}
  // return fib(n-2)+fib(n-1)

  // sol3 O(n), O(n) 73~76ms 76~73%보다 빠름
  // tabulation
  // cache = Array.from({length : 100}, (v)=>{return 0})
  // cache[1] = 1
  // for (let i=2; i < n+1; i++){
  //   cache[i] = cache[i-2]+cache[i-1]
  // }
  // return cache[n]

  // sol4 O(n), O(n) 57~76ms 95~73%보다 빠름
  // memoization
// var hashMap = {"0" : 0, "1" : 1}
  // if (hashMap[n] != undefined) {return hashMap[n]}
  // else{
  //   hashMap[n] = fib(n-1)+fib(n-2)
  //   return hashMap[n]
  // }

  // sol5 O(logn) 60~115ms 95~28%보다 빠름
  // n=2000이면 infinity, n=3000이면 NaN
  // isInfinite()를 사용하면 -infinity, infinity인지 확인 가능하다.
  // isNaN()을 사용하면 NaN인지 확인가능
  // 숫자가 아닌 연산일 경우 NaN을 반환하는 데 

  if (n <= 1){ return n; }
  var matrix = [[1,1], [1,0]]
  matrixPower(matrix, n-1)
  return matrix[0][0]
};

var matrixPower = function(matrix, n){
  if ( n <= 1 ) { return matrix }
  matrixPower(matrix, parseInt(n/2))

  matrixMultiply(matrix, matrix)
  basicMatrix = [[1,1],[1,0]]
  if (n%2==1){
    matrixMultiply(matrix, basicMatrix)
  }

}
var matrixMultiply = function (a,b) {
  w = a[0][0]*b[0][0] + a[0][1]*b[1][0]
  x = a[0][0]*b[0][1] + a[0][1]*b[1][1]
  y = a[1][0]*b[0][0] + a[1][1]*b[1][0]
  z = a[1][0]*b[0][1] + a[1][1]*b[1][1]

  a[0][0] = w
  a[0][1] = x
  a[1][0] = y
  a[1][1] = z
}
var startTime = new Date().getTime()
console.log(fib(3000))
var endTime = new Date().getTime()
console.log(endTime-startTime)
