#!/usr/bin/node

// Wait for the document to be ready
$(document).ready(function () {
  // Select the <header> element
  const headerElement = $('header');

  // Add a click event listener to the <div> with ID "toggle_header"
  $('#toggle_header').click(function () {
    // Toggle the class between "red" and "green"
    headerElement.toggleClass('red green');
  });
});
