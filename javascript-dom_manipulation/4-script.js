// Task 4: List of elements
// This script adds a li element to a list when the user clicks on the element
// with id add_item. The new element must be: <li>Item</li>
// The new element must be added to the ul element with class my_list

// Select the element with id 'add_item' using document.getElementById
// This method returns the element with the specified ID
const addItem = document.getElementById('add_item');

// Add a click event listener to the add_item element
// When clicked, it will execute the function that adds a new list item
addItem.addEventListener('click', function() {
    // Select the ul element with class 'my_list'
    const list = document.querySelector('ul.my_list');
    
    // Create a new li element
    const newItem = document.createElement('li');
    
    // Set the text content of the new li element
    newItem.textContent = 'Item';
    
    // Append the new li element to the ul list
    list.appendChild(newItem);
}); 