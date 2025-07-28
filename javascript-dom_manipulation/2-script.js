// Task 2: Add .red class
// This script adds the class red to the header element when the user clicks
// on the tag with id red_header

// Select the element with id 'red_header' using document.getElementById
// This method returns the element with the specified ID
const redHeader = document.getElementById('red_header');

// Add a click event listener to the red_header element
// When clicked, it will execute the function that adds the red class
redHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');
    
    // Add the 'red' class to the header element
    // This will apply the CSS style color: #FF0000
    header.classList.add('red');
}); 