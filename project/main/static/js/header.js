// header.js
$(function() {
  var prevScrollPosition = $(window).scrollTop();

  $(window).scroll(function() {
    var currentScrollPosition = $(window).scrollTop();
    var header = $('header');

    if (prevScrollPosition > currentScrollPosition) {
      header.css('background-color', 'black').fadeIn('slow');
    } else {
      header.fadeOut('slow');
    }

    prevScrollPosition = currentScrollPosition;
  });
});
