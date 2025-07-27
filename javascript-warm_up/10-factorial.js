#!/usr/bin/node

/**
 * Task 10: Factorial
 *
 * This script demonstrates:
 * - How to implement recursive functions in JavaScript
 * - How to handle base cases in recursion
 * - How to convert arguments to integers
 * - Mathematical operations with recursion
 *
 * Requirements:
 * - Compute and print factorial of first argument
 * - Factorial of NaN is 1
 * - Must be done recursively
 * - Must use a function
 * - Don't use 'var' keyword
 */

// Define the factorial function recursively
function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

// Get the first argument and convert it to integer
const arg = parseInt(process.argv[2]);

// Print the factorial result
console.log(factorial(arg));
