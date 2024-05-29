// Fetches and displays "Hello" translation based on language code using jQuery
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
