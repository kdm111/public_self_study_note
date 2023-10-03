var compose = function(functions) {
  // sol1 65ms 88% 43.2MB 76%
	// return function(x) {
  //   for (let i = functions.length-1; i >= 0; i--) {
  //     x = functions[i](x)
  //   }
  //   return x
  // }

  // 69ms 73% 43.4MB 56%
  return x => functions.reduceRight((acc, fun) => fun(acc), x)
};

functions = [x => x+1, x => x * x, x => 2 * x]; x = 4
