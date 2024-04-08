#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const nums = process.argv.slice(2).map(Number);
  nums.sort((a, b) => a - b);
  console.log(nums[nums.length - 2]);
}
