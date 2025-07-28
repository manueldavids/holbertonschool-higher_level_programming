// Task 6: Star wars character
// This script fetches the character name from the Star Wars API
// and displays it in the HTML element with id character
// Must use the Fetch API

// Fetch data from the Star Wars API
// This returns a Promise that resolves with the response
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function(response) {
        // Check if the response is ok (status 200-299)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON response
        return response.json();
    })
    .then(function(data) {
        // Select the element with id 'character'
        const characterElement = document.getElementById('character');
        
        // Display the character name from the API response
        characterElement.textContent = data.name;
    })
    .catch(function(error) {
        // Handle any errors that occurred during the fetch
        console.error('Error fetching character data:', error);
        
        // Display error message in the character element
        const characterElement = document.getElementById('character');
        characterElement.textContent = 'Error loading character data';
    }); 