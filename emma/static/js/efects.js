function detectTouch(e) {
  $('#navbar-trigger').prop('checked', false);
}

$(function() {
	$('section').click(function () {
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
		document.getElementsByTagName('section')[0].addEventListener('touchmove', detectTouch, false);
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
          document.getElementsByTagName('section')[0].addEventListener('touchmove', detectTouch, false);
        } else {
          document.getElementsByTagName('section')[0].removeEventListener('touchmove', detectTouch, false);
        }
    });
});
