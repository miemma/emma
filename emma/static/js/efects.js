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
	} else {
	  $('#benefitscollapse').removeClass('collapse');
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

    $('#reservation-time-button').click(function () {
        button_time = document.getElementById('reservation-time-button');
        if (button_time.value == 'AM') {
            button_time.value = 'PM';
        } else if (button_time.value == 'PM') {
            button_time.value = 'AM';
        }
    });

    $('#datepicker').datepicker()
        .on('changeDate', function(e) {
            $('#date_input').val(
                $('#datepicker').datepicker('getFormattedDate')
            )
        });

    input = document.getElementsByName("number");
    input.addEventListener("mousewheel", function(event){ this.blur() });

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
