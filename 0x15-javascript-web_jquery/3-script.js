// Adds "red" class to header on click using jQuery
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
