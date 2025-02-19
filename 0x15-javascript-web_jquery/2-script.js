// Wait for the document to be ready
$(document).ready(() => {
    // Select the red_header div and attach a click handler
    const $redHeader = $('#red_header');
    
    // Add click event listener
    $redHeader.on('click', () => {
        // Select the header element and change its color to red
        $('header').css('color', '#FF0000');
    });
});
