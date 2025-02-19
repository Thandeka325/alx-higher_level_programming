// Wait for the document to be ready
$(document).ready(() => {
    // Select the toggle_header div and attach a click handler
    const $toggleHeader = $('#toggle_header');
    
    // Add click event listener
    $toggleHeader.on('click', () => {
        // Select the header element
        const $header = $('header');
        
        // Toggle between red and green classes
        if ($header.hasClass('red')) {
            $header.removeClass('red').addClass('green');
        } else {
            $header.removeClass('green').addClass('red');
        }
    });
});
