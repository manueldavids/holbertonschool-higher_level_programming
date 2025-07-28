// Task 7: Star Wars movies
// This script fetches and lists the title for all movies using the Star Wars API
// All movie titles must be listed in the HTML ul element with id list_movies
// Must use the Fetch API

// Fetch data from the Star Wars API for all films
// This returns a Promise that resolves with the response
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        // Check if the response is ok (status 200-299)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON response
        return response.json();
    })
    .then(function(data) {
        // Select the ul element with id 'list_movies'
        const listMovies = document.getElementById('list_movies');
        
        // Iterate through all movies in the results array
        data.results.forEach(function(movie) {
            // Create a new li element for each movie
            const listItem = document.createElement('li');
            
            // Set the text content to the movie title
            listItem.textContent = movie.title;
            
            // Append the li element to the ul list
            listMovies.appendChild(listItem);
        });
    })
    .catch(function(error) {
        // Handle any errors that occurred during the fetch
        console.error('Error fetching movies data:', error);
        
        // Display error message in the list
        const listMovies = document.getElementById('list_movies');
        const errorItem = document.createElement('li');
        errorItem.textContent = 'Error loading movies data';
        listMovies.appendChild(errorItem);
    }); 