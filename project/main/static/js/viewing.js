// // function isVisible($el) {
// //   let docViewTop = $(window).scrollTop();
// //   let docViewBottom = docViewTop + $(window).height();
// //   let elTop = $el.offset().top;
// //   let elBottom = elTop + $el.height();
// //   return ((elBottom <= docViewBottom) && (elTop >= docViewTop));
// // }

// // $(function() {
// //   // Обработчик событий для изменения фона кнопок при отображении якорей
// //   $(window).scroll(function() {
// //     $('.nav-btn').each(function() {
// //       if (isVisible($($(this).attr('href')))) {
// //         $(this).addClass('active');
// //       } else {
// //         $(this).removeClass('active');
// //       }
// //     });
// //   });
// // });


function updateButtonState() {
  $('.nav-btn').each(function() {
    let target = $($(this).attr('href'));
    if (target.length) {
      let position = target.offset().top - $(window).scrollTop();
      let height = target.outerHeight();
      if (position <= 100 && position + height > 100) {
        $(this).addClass('active');
      } else {
        $(this).removeClass('active');
      }
    }
  });
}

$(document).ready(function() {
  $(window).scroll(function() {
    updateButtonState();
  });
  updateButtonState();
});



// function updateActiveSection() {
//   $('.title').each(function() {
//     let position = $(this).offset().top - $(window).scrollTop();
//     let height = $(this).outerHeight();
//     if (position <= 0 && position + height > 0) {
//       $(this).addClass('active');
//     } else {
//       $(this).removeClass('active');
//     }
//   });
// }

// $(document).ready(function() {
//   $(window).scroll(function() {
//     updateActiveSection();
//   });
//   updateActiveSection();
// });
