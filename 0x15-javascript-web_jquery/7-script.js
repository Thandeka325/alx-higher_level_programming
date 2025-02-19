// Wait for the document to be ready
$(document).ready(() => {
    // Select the character div
    const $characterDiv = $('#character');
    
    // Make the AJAX request to fetch character data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: (data) => {
            // Update the div with the character's name
            $characterDiv.text(data.name);
        },
        error: (xhr, status, error) => {
            // Handle any errors that occur
            $characterDiv.text('Failed to fetch character data');
        }
    });
});
