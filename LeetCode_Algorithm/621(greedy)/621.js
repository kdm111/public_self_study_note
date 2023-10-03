var leastInterval = function(tasks, n) {
  // sol1 121ms 83%
  let arr = new Array(26).fill(0)
  for (let task of tasks) {
    arr[task.charCodeAt(0)-65] += 1
  }
  arr.sort((a,b) => {
    return a-b
  })
  let max_v = arr.pop();
  console.log(arr)
  let idle_time = (max_v-1) * n
  while (arr.length > 0 && idle_time > 0) {
    idle_time -= Math.min(arr.pop(), max_v-1)
  }
  if (idle_time < 0) {idle_time = 0}
  return tasks.length + idle_time
};

console.log(leastInterval(['A', 'B', 'B', 'A', 'B', 'A'], 2))
