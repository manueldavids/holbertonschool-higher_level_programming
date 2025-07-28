// Task 5: Change the text
// This script updates the text of the header element to "New Header!!!"
// when the user clicks on the element with id update_header

// Select the element with id 'update_header' using document.getElementById
// This method returns the element with the specified ID
const updateHeader = document.getElementById('update_header');

// Add a click event listener to the update_header element
// When clicked, it will execute the function that updates the header text
updateHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');
    
    // Update the text content of the header to "New Header!!!"
    header.textContent = 'New Header!!!';
}); 