// Wait for the document to be ready
$(document).ready(() => {
    // Select the add_item div and attach a click handler
    const $addItem = $('#add_item');
    
    // Add click event listener
    $addItem.on('click', () => {
        // Create new list item
        const $newItem = $('<li>Item</li>');
        
        // Add the new item to the list
        $('.my_list').append($newItem);
    });
});
