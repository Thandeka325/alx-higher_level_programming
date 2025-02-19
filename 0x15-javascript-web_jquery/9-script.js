// Wait for the document to be ready
$(document).ready(() => {
    // Select the hello div
    const $helloDiv = $('#hello');
    
    // Make the AJAX request to fetch the translation
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: (data) => {
            // Display the translation in the div
            $helloDiv.text(data.hello);
        },
        error: (xhr, status, error) => {
            // Handle any errors that occur
            $helloDiv.text('Failed to fetch translation');
        }
    });
});
