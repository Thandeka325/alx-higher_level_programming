// Wait for the document to be ready
$(document).ready(() => {
    // Select the input elements and div
    const $languageCode = $('#language_code');
    const $translateBtn = $('#btn_translate');
    const $helloDiv = $('#hello');
    
    // Add click handler for the translate button
    $translateBtn.on('click', () => {
        // Get the language code from the input
        const languageCode = $languageCode.val().toLowerCase();
        
        // Make the AJAX request to fetch the translation
        $.ajax({
            url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
            type: 'GET',
            success: (data) => {
                // Display the translation in the div
                $helloDiv.text(data.hello);
            },
            error: (xhr, status, error) => {
                // Handle any errors that occur
                $helloDiv.text('Translation not found');
            }
        });
    });
});
