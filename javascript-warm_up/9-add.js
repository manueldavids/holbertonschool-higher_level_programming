#!/usr/bin/node

/**
 * Task 9: Add
 *
 * This script demonstrates:
 * - How to define functions in JavaScript
 * - How to convert arguments to integers
 * - How to handle function parameters
 * - Basic arithmetic operations
 *
 * Requirements:
 * - Print the addition of 2 integers
 * - First argument is the first integer
 * - Second argument is the second integer
 * - Define function with prototype: function add(a, b)
 * - Don't use 'var' keyword
 */

// Define the add function as required
function add (a, b) {
  return a + b;
}

// Get the two arguments and convert them to integers
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Print the result of the addition
console.log(add(arg1, arg2));
