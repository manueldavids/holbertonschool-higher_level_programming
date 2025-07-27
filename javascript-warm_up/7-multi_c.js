#!/usr/bin/node

/**
 * Task 7: I love C
 *
 * This script demonstrates:
 * - How to convert arguments to integers
 * - How to validate input before processing
 * - How to use loops for repeated output
 * - How to handle invalid input gracefully
 *
 * Requirements:
 * - Print "C is fun" x times (x = first argument)
 * - Print "Missing number of occurrences" if invalid input
 * - Use only two console.log() statements
 * - Use a loop (while, for, etc.)
 * - Don't use 'var' keyword
 */

// Get the first argument and convert it to integer
const arg = process.argv[2];
const times = parseInt(arg);

// Check if the conversion was successful (only invalid inputs, not negative numbers)
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else if (times > 0) {
  // Use a for loop to print "C is fun" the specified number of times
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
