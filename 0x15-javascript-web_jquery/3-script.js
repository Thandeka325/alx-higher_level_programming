// Wait for the document to be ready
$(document).ready(() => {
    // Select the red_header div and attach a click handler
    const $redHeader = $('#red_header');
    
    // Add click event listener
    $redHeader.on('click', () => {
        // Select the header element and add the red class
        $('header').addClass('red');
    });
});
