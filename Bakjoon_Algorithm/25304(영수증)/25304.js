const fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().split("\n")
// const input = fs.readFileSync("test.txt").toString().split("\n")

const total = parseInt(input[0])
let temp = 0
for (let i = 2; i < input.length; i++) {
  if (input[i] != '') {
    let inp = input[i].split(' ').map((a) => {
      return parseInt(a)
    })
    temp += (inp[0] * inp[1])
  }
}

total == temp ? console.log("Yes") : console.log("No")