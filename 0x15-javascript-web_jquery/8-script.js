// Fetches and lists all Star Wars movie titles using jQuery
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
