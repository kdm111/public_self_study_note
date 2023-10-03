var argumentsLength = function(...args) {
  // sol1 50ms 91% 42.1MB 26%
  return args.length
};

console.log(argumentsLength([{}, null, "3"]))