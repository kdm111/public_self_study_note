const fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().split(' ')

let a = Number(input[0]); let b = Number(input[1]); let c = Number(input[2])
if ((a == b) && (b == c)) {
  console.log(10000 + 1000 * a)
} else if (a == b) {
  console.log(1000 + 100 * a)
} else if (b == c) {
  console.log(1000 + 100 * b)
} else if (c == a) {
  console.log(1000 + 100 * c)
} else {
  let m = Math.max(a,b,c)
  console.log(m * 100)
}
