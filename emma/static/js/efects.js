function detectTouch(e) {
  $('#navbar-trigger').prop('checked', false);
}

$(function() {
	$('#content-no-navbar-wrapper').click(function () {
		$('#navbar-trigger').prop('checked', false);
	});

	var movile = window.matchMedia( "(max-width: 768px)" );
	var responsiveMenu = window.matchMedia( "(max-width: 1100px)" );

	if (movile.matches) {
	  $('#benefitscollapse').addClass('collapse');
      $('#successBtn').text('Inicio')
	} else {
	  $('#benefitscollapse').removeClass('collapse');
        $('#successBtn').text('Regresar a la página principal')
	}

	if (responsiveMenu.matches) {
		document.getElementById('content-no-navbar-wrapper').addEventListener('touchmove', detectTouch, false);
	}

	$(window).scroll(function () {
		$(this).scrollTop() < 20 ?
	    $('header').removeClass('header-navbar-white'):
			$('header').addClass('header-navbar-white');
	});

	$(window).scroll(function () {
		$(this).scrollTop() < 20 ?
	    $('li[hcolor="white"]').removeClass('white'):
			$('li[hcolor="white"]').addClass('white');
	});

    $( window ).resize(function() {
        //noinspection JSUnresolvedFunction
        var movile = window.matchMedia( "(max-width: 768px)" );
        var responsiveMenu = window.matchMedia( "(max-width: 1100px)" );
        if (movile.matches) {
            $('#benefitscollapse').addClass('collapse');
        } else {
            $('#benefitscollapse').removeClass('collapse');
            $('#navbar-trigger').prop('checked', false);
        }
        if (responsiveMenu.matches) {
          document.getElementById('content-no-navbar-wrapper').addEventListener('touchmove', detectTouch, false);
        } else {
          document.getElementById('content-no-navbar-wrapper').removeEventListener('touchmove', detectTouch, false);
        }
    });
});

$('.dashboard-toggle-list-button').click(function () {
  if ($(this).hasClass('inverse')) {
    $($(this).parent().parent()
      .siblings('.dashboard-toggle-list-content'))
      .removeClass('toggle');
    $(this).removeClass('inverse');
  } else {
    $($(this).parent().parent()
      .siblings('.dashboard-toggle-list-content'))
      .addClass('toggle');
    $(this).addClass('inverse');
  }
});
