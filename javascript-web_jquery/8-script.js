#!/usr/bin/node
// Wait for the document to be ready
$(document).ready(function () {
  // Make an AJAX request to fetch data from the specified URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the movie titles from the response
    const movieTitles = data.results.map(movie => movie.title);

    // Create a new <li> element for each movie title
    movieTitles.forEach(title => {
      const listItem = $('<li>').text(title);
      $('#list_movies').append(listItem);
    });
  });
});
