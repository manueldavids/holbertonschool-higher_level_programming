#!/usr/bin/node

/**
 * Task 2: Arguments
 *
 * This script demonstrates:
 * - How to access command line arguments using process.argv
 * - How to use conditional statements (if/else)
 * - How to count array elements
 * - Basic logic flow control
 *
 * Requirements:
 * - Print "No argument" if no arguments passed
 * - Print "Argument found" if one argument passed
 * - Print "Arguments found" if multiple arguments passed
 * - Don't use 'var' keyword
 * - Use process.argv to access arguments
 */

// Get the number of actual arguments (excluding node and script path)
const argumentCount = process.argv.length - 2;

// Check the number of arguments and print appropriate message
if (argumentCount === 0) {
  console.log('No argument');
} else if (argumentCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
