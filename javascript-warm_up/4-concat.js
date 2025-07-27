#!/usr/bin/node

/**
 * Task 4: Create a sentence
 *
 * This script demonstrates:
 * - How to concatenate strings with template literals or + operator
 * - How to handle undefined arguments gracefully
 * - How to format output with specific structure
 * - Basic string manipulation in JavaScript
 *
 * Requirements:
 * - Print two arguments in format: "arg1 is arg2"
 * - Handle undefined arguments by printing "undefined"
 * - Don't use 'var' keyword
 */

// Get the two arguments (they might be undefined)
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Print the formatted sentence
console.log(arg1 + ' is ' + arg2); 