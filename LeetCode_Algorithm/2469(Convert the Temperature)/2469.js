var convertTemperature = function(celsius) {
  // sol1 61ms 66.9% 42.3MB 16%
  return [celsius + 273.15, celsius * 1.8 + 32]
};