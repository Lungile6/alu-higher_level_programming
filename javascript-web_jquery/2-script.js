#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with the ID "red_header"
  const redHeaderDiv = $('#red_header');

  // Add a click event listener to the selected <div>
  redHeaderDiv.click(function () {
    // Update the text color of the <header> element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
