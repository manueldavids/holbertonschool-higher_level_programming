// Task 1: Click and turn red
// This script updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id red_header

// Select the element with id 'red_header' using document.getElementById
// This method returns the element with the specified ID
const redHeader = document.getElementById('red_header');

// Add a click event listener to the red_header element
// When clicked, it will execute the function that changes the header color
redHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');
    
    // Change the text color to red (#FF0000)
    header.style.color = '#FF0000';
}); 