const fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().split("\n")

let k = Number(input[1])
console.log(input[0][k-1])
