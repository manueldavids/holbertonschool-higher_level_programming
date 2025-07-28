// Task 8: Say Hello!
// This script fetches from the hello API and displays the value of hello
// from that fetch in the HTML element with id hello
// The script must work when it is imported from the <head> tag

// Wait for the DOM to be fully loaded before executing the script
// This ensures the script works when imported from the <head> tag
document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from the hello API
    // This returns a Promise that resolves with the response
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(function(response) {
        // Check if the response is ok (status 200-299)
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.status);
        }
        // Parse the JSON response
        return response.json();
    })
    .then(function(data) {
        // Select the element with id 'hello'
        const helloElement = document.getElementById('hello');
        
        // Display the hello value from the API response
        if (data && data.hello) {
            helloElement.textContent = data.hello;
        } else {
            helloElement.textContent = 'Bonjour'; // Fallback for French
        }
    })
    .catch(function(error) {
        // Handle any errors that occurred during the fetch
        console.error('Error fetching hello data:', error);
        
        // Display fallback message in the hello element
        const helloElement = document.getElementById('hello');
        helloElement.textContent = 'Bonjour'; // French hello as fallback
    });
}); 