#!/usr/bin/node

/**
 * Task 8: Square
 *
 * This script demonstrates:
 * - How to create nested loops for 2D patterns
 * - How to build strings with repeated characters
 * - How to validate input for square dimensions
 * - How to handle invalid input gracefully
 *
 * Requirements:
 * - Print a square using 'X' characters
 * - First argument is the size of the square
 * - Print "Missing size" if invalid input
 * - Use 'X' character to print the square
 * - Use a loop (while, for, etc.)
 * - Don't use 'var' keyword
 */

// Get the first argument and convert it to integer
const arg = process.argv[2];
const size = parseInt(arg);

// Check if the conversion was successful
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  // Use nested loops to create the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
