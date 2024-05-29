// Adds new list item on click using jQuery
$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
