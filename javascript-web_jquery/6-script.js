#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with the ID "update_header"
  const updateHeaderDiv = $('#update_header');

  // Add a click event listener to the selected <div>
  updateHeaderDiv.click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
