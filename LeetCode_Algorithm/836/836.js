var isRectangleOverlap = function(rec1, rec2) {
  // sol1 O(1), O(1) 60~67ms 88~66%
  var x_intersect = (rec1[0] < rec2[2] && rec2[0] < rec1[2])
  var y_intersect = (rec1[1] < rec2[3] && rec2[1] < rec1[3])
  return x_intersect && y_intersect
};
console.log(isRectangleOverlap([1,1,3,3], [0,0,2,2]))