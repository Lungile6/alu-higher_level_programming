#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Make an AJAX request to fetch data from the specified URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the response
    const characterName = data.name;

    // Display the character name in the <div> with ID "character"
    $('#character').text(characterName);
  });
});
