// Wait for the document to be ready
$(document).ready(() => {
    // Select the list and control elements
    const $list = $('.my_list');
    const $addItem = $('#add_item');
    const $removeItem = $('#remove_item');
    const $clearList = $('#clear_list');
    
    // Add click handler for adding items
    $addItem.on('click', () => {
        // Create new list item and add to the end of the list
        $list.append('<li>Item</li>');
    });
    
    // Add click handler for removing items
    $removeItem.on('click', () => {
        // Remove the last item from the list
        $list.find('li:last').remove();
    });
    
    // Add click handler for clearing the list
    $clearList.on('click', () => {
        // Remove all items from the list
        $list.empty();
    });
});
