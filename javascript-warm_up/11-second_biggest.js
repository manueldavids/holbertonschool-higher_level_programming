#!/usr/bin/node

/**
 * Task 11: Second biggest!
 *
 * This script demonstrates:
 * - How to process multiple command line arguments
 * - How to find the second largest value in an array
 * - How to handle edge cases (no args, one arg)
 * - Array manipulation and sorting techniques
 *
 * Requirements:
 * - Search the second biggest integer in the list of arguments
 * - All arguments can be converted to integer
 * - If no argument passed, print 0
 * - If the number of arguments is 1, print 0
 * - Don't use 'var' keyword
 */

// Get all arguments starting from index 2 (skip node and script path)
const args = process.argv.slice(2);

// Check if we have enough arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to integers
  const numbers = args.map(arg => parseInt(arg));

  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);

  // Remove duplicates by creating a Set and converting back to array
  const uniqueNumbers = [...new Set(numbers)];

  // Print the second biggest number (index 1) or 0 if only one unique number
  console.log(uniqueNumbers.length > 1 ? uniqueNumbers[1] : 0);
}
