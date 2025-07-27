#!/usr/bin/node

/**
 * Task 13: Add file
 *
 * This script demonstrates:
 * - How to create functions that can be exported
 * - How to use module.exports for Node.js modules
 * - How to make functions visible from outside
 * - Basic function export patterns
 *
 * Requirements:
 * - Write a function that returns the addition of 2 integers
 * - The function must be visible from outside
 * - The name of the function must be 'add'
 * - Don't use 'var' keyword
 */

// Define the add function
function add (a, b) {
  return a + b;
}

// Export the function to make it visible from outside
module.exports = { add };
