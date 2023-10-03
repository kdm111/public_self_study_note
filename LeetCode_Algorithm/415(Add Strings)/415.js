var addStrings = function(num1, num2) {
    // sol1 68~98ms, 95~58%보다 빠름
    // js는 내부적으로 부동 소수점을 사용하고 
    // 2^53보다 절대값이 큰 양수 음수는 number로 표기가 될 수 없다.
    // 약 9000조 이상
    // console.log(num1)
    // console.log(Number(num1))
    // return Number(num1) + Number(num2)

    // 비트 연산자와 시프트 연산자는 32비트 정수에서 작동하므로 2^31-1 까지가 최대 안전 정수이다.
    // 비트 연산자 (&&, ||, ^, ~)
    // 시프트 연산자(<<, >>)
    // 따라서 큰 수를 표현할 때 사용되는 BigInt를 사용한다.
    // console.log(BigInt(num1))
    // console.log(BigInt(num2))
    // return String(BigInt(num1)+BigInt(num2))

    // sol2
    // 이 방법으로는 bitint를 만들 수 없음
    // var n1 = 0
    // var n2 = 0
    // // codePointAt()은 문자를 아스키 코드로 바꾼 값을 리턴한다.
    // for (i of num1){
    //     n1 = n1*10 + i.codePointAt() - "0".codePointAt()
    // }
    // console.log(n1)

  // sol3 76~105ms 85~46%  
  var ans = ""

  var carry = 0
  var num1Pointer = num1.length-1
  var num2Pointer = num2.length-1

  while (num1Pointer >= 0 || num2Pointer >= 0){
    let v1 = 0
    let v2 = 0
    if (num1Pointer >= 0){
      v1 = num1[num1Pointer].codePointAt() - "0".codePointAt()
    }
    if (num2Pointer >= 0){
      v2 = num2[num2Pointer].codePointAt() - "0".codePointAt()
    }

    let r = v1+v2+carry
    // if ((r/10) >= 1){carry = parseInt(r/10)}
    // else{carry = 0}
    r/10 >= 1 ? carry = parseInt(r/10) : carry = 0
    ans += String(r%10)
    num1Pointer -= 1 
    num2Pointer -= 1
  }
  if (carry > 0){
    ans += carry
  }

  return ans.split("").reverse().join("")

};

console.log(addStrings("456", "77"))