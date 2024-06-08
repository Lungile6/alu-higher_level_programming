#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Select the <div> with the ID "add_item"
  const addItemDiv = $('#add_item');

  // Add a click event listener to the selected <div>
  addItemDiv.click(function () {
    // Create a new <li> element with the text "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the existing UL.my_list
    $('ul.my_list').append(newItem);
  });
});
