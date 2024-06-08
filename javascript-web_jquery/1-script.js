#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Select the <header> element using jQuery
  const headerElement = $('header');

  // Update the text color to red (#FF0000)
  headerElement.css('color', '#FF0000');
});
