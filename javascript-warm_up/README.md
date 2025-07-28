# JavaScript - Warm Up

This project contains a series of JavaScript scripts designed to introduce fundamental JavaScript concepts and programming practices. Each script demonstrates different aspects of JavaScript programming, from basic syntax to more advanced concepts like functions, objects, and modules.

## Learning Objectives

By completing this project, you will be able to explain to anyone, without the help of Google:

### General Concepts
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- Differences between var, const and let
- All data types available in JavaScript
- How to use if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use while and for loops
- How to use break and continue statements
- What is a function and how to use functions
- What does a function that does not use any return statement return
- Scope of variables
- Arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Project Structure

The project consists of 13 JavaScript scripts, each focusing on specific concepts:

### Basic Scripts (Tasks 0-5)
- **0-javascript_is_amazing.js**: First constant and print
- **1-multi_languages.js**: Print multiple lines
- **2-arguments.js**: Handle command line arguments
- **3-value_argument.js**: Access first argument value
- **4-concat.js**: Concatenate arguments
- **5-to_integer.js**: Convert and validate integers

### Control Flow (Tasks 6-8)
- **6-multi_languages_loop.js**: Use arrays and loops
- **7-multi_c.js**: Print repeated messages with loops
- **8-square.js**: Create 2D patterns with nested loops

### Functions and Logic (Tasks 9-11)
- **9-add.js**: Function to add two integers
- **10-factorial.js**: Recursive factorial function
- **11-second_biggest.js**: Find second largest value

### Objects and Modules (Tasks 12-13)
- **12-object.js**: Object property manipulation
- **13-add.js**: Module with exported function

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All files end with a new line
- First line of all files is exactly `#!/usr/bin/node`
- All files are executable
- Code follows semistandard style (version 16.x.x)

### Code Style
- Use semicolons
- Follow AirBnB style guide
- No trailing spaces
- Files must end with newline
- Use const and let instead of var

## Installation and Setup

### Install Node.js 14
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semistandard
```bash
sudo npm install semistandard --global
```

## Usage Examples

### Running Scripts
```bash
# Make script executable
chmod +x script_name.js

# Run script
./script_name.js

# Run with arguments
./script_name.js arg1 arg2
```

### Style Checking
```bash
# Check style
semistandard script_name.js

# Fix style automatically
semistandard --fix script_name.js
```

## Key Concepts Demonstrated

### Variables and Constants
- Using `const` for immutable values
- Using `let` for mutable variables
- Avoiding `var` keyword

### Control Flow
- Conditional statements (if/else)
- Loops (for, while)
- Break and continue statements

### Functions
- Function declarations
- Parameters and return values
- Recursive functions
- Function scope

### Data Structures
- Arrays and array methods
- Objects and object properties
- Sets for unique values

### Modules
- Exporting functions
- Importing modules
- CommonJS module system

### Command Line Arguments
- Accessing `process.argv`
- Converting arguments to appropriate types
- Handling missing arguments

## Testing

Each script can be tested independently:

```bash
# Test basic functionality
./0-javascript_is_amazing.js
# Expected output: JavaScript is amazing

# Test with arguments
./2-arguments.js Best School
# Expected output: Arguments found

# Test function export
./13-main.js
# Expected output: 8
```

## Best Practices

- Always validate input before processing
- Handle edge cases (missing arguments, invalid input)
- Use meaningful variable names
- Add comments to explain complex logic
- Follow consistent code style
- Test scripts with various inputs

## Author

This project is part of the Holberton School curriculum, designed to teach fundamental JavaScript concepts through practical exercises.

## License

This project is for educational purposes as part of the Holberton School program.
