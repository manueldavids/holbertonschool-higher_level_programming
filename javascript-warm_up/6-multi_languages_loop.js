#!/usr/bin/node

/**
 * Task 6: Loop to languages
 *
 * This script demonstrates:
 * - How to use arrays in JavaScript
 * - How to iterate through arrays with loops
 * - How to use a single console.log() with loop
 * - Basic array manipulation and iteration
 *
 * Requirements:
 * - Print "C is fun", "Python is cool", "JavaScript is amazing"
 * - Use an array of strings
 * - Use a loop (while, for, etc.)
 * - Use only one console.log()
 * - Don't use 'var' keyword
 * - Don't use if/else statements
 */

// Create an array with the three programming languages
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

// Use a for loop to iterate through the array
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
}
