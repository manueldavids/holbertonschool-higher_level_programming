#!/usr/bin/node

/**
 * Task 3: Value of my argument
 *
 * This script demonstrates:
 * - How to access the first command line argument
 * - How to check if arguments exist without using length
 * - Basic conditional logic for argument handling
 * - String output based on argument presence
 *
 * Requirements:
 * - Print the first argument passed to the script
 * - If no arguments passed, print "No argument"
 * - Don't use 'var' keyword
 * - Don't use 'length' property
 */

// Check if there's a first argument (index 2 in process.argv)
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
} 