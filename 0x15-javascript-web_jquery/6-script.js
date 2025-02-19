// Wait for the document to be ready
$(document).ready(() => {
    // Select the update_header div and attach a click handler
    const $updateHeader = $('#update_header');
    
    // Add click event listener
    $updateHeader.on('click', () => {
        // Update the header text
        $('header').text('New Header!!!');
    });
});
