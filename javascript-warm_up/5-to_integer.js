#!/usr/bin/node

/**
 * Task 5: An Integer
 *
 * This script demonstrates:
 * - How to convert strings to integers using parseInt()
 * - How to check if a value is NaN (Not a Number)
 * - How to handle type conversion errors
 * - Basic input validation and type checking
 *
 * Requirements:
 * - Convert first argument to integer
 * - Print "My number: <number>" if conversion successful
 * - Print "Not a number" if conversion fails
 * - Don't use 'var' keyword
 * - Don't use try/catch
 */

// Get the first argument and convert it to integer
const arg = process.argv[2];
const number = parseInt(arg);

// Check if the conversion was successful
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
