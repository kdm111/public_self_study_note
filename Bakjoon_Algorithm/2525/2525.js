const fs = require('fs')
// const input = fs.readFileSync("test.txt").toString().split("\n")
const input = fs.readFileSync("/dev/stdin").toString().split("\n")


inp = input[0].split(" ")
let m = Number(inp[0]); let n = Number(inp[1])
let k = Number(input[1])

n += k
if (n >= 60) {
  m += parseInt(n / 60)
  n %= 60
  if (m >= 24) {
    m %= 24
  }
}
console.log(m, n)

