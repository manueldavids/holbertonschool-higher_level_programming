// Task 3: Toggle classes
// This script toggles the class of the header element when the user clicks
// on the tag id toggle_header. The header must always have one class: red or green,
// never both in the same time and never empty.

// Select the element with id 'toggle_header' using document.getElementById
// This method returns the element with the specified ID
const toggleHeader = document.getElementById('toggle_header');

// Add a click event listener to the toggle_header element
// When clicked, it will execute the function that toggles the header class
toggleHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');
    
    // Check if the header currently has the 'red' class
    if (header.classList.contains('red')) {
        // If it has 'red', remove it and add 'green'
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        // If it has 'green' (or no class), remove 'green' and add 'red'
        header.classList.remove('green');
        header.classList.add('red');
    }
}); 