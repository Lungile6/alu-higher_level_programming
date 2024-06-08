#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Make an AJAX request to fetch data from the specified URL
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Extract the translated "hello" from the response
    const translatedHello = data.hello;

    // Display the translated "hello" in the <div> with ID "hello"
    $('#hello').text(translatedHello);
  });
}); i;
