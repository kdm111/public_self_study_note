const fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().split('\n')
// const input = fs.readFileSync("test.txt").toString().split('\n')

const numbers = input[1].split(" ")
let d = new Map()
for (let n of numbers) {
  if (d.has(n)) {
    d.set(n, d.get(n) + 1)
  } else {
    d.set(n, 1)
  }
}

console.log(d.get(input[2]) == undefined ? 0 : d.get(input[2]))