// Toggles header class between "red" and "green" using jQuery
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
