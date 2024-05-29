// Fetches and displays "Hello" translation on button click or "Enter" key press using jQuery
$(document).ready(function () {
  function translateHello() {
    const languageCode = $('#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translateHello();
    }
  });
});
