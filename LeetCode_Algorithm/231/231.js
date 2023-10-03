var isPowerOfTwo = function(n) {
  
  // sol1 O(logn), O(1) 116~124ms 25~17%
  // if (n==0){return false}
  // var idx = 0
  // while (n % 2 == 0){
  //   n /= 2
  //   idx += 1
  // }
  // console.log(idx)
  // return n==1

  // sol2 
  // js의 이진 비트 연산은 부호 있는 32비트 정수값으로 정의된다.
  // -2,147,483,648
  // 2,137,483,647 32비트 부호 정수형 최대값  == 2^31-1
  // 많은 언어에서 int가 지원하는 최대 값
  // -2,147,483,648은 -2^32이다.
  // 따라서 제대로 된 구현을 위해선 bigInt를 사용한다.
  // if (n==0){return false}
  // var num = BigInt(n)
  // return (num & -num) == num


  
  // sol3
  // -2147483648에서 실패함
  // if (n==0){return false}
  // return (n & n-1) == 0
  
  // sol4  91ms 79% 43.7MB 53%
  // O(1) O(1)
  if (n == 0) {return false}
  return (BigInt(n) & BigInt(n) - BigInt(1)) == 0
};

console.log(isPowerOfTwo(22147483648))