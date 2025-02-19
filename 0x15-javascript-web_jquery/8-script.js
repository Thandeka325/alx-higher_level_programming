// Wait for the document to be ready
$(document).ready(() => {
    // Select the movies list
    const $moviesList = $('#list_movies');
    
    // Make the AJAX request to fetch movies data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: (data) => {
            // Clear any existing content
            $moviesList.empty();
            
            // Loop through each movie and add to the list
            $.each(data.results, (index, movie) => {
                $moviesList.append(`<li>${movie.title}</li>`);
            });
        },
        error: (xhr, status, error) => {
            // Handle any errors that occur
            $moviesList.html('<li>Failed to fetch movie data</li>');
        }
    });
});
