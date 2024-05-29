// Fetches and displays "Hello" in French using jQuery
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
