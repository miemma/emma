(function () {
	$.fn.datepicker.dates['en'] = {
	  days: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"],
	  daysShort: ["Dom", "Lun", "Mar", "Mier", "Jue", "Vie", "Sab"],
	  daysMin: ["D", "L", "M", "M", "J", "V", "S"],
	  months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
	  monthsShort: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
	  today: "Hoy",
	  clear: "Limpiar",
	  format: "mm/dd/yyyy",
	  titleFormat: "MM yyyy", /* Leverages same syntax as 'format' */
	  weekStart: 1
	};

	var datepickers = '#datepicker, #call-modal-datepicker, #appointment-modal-datepicker, #customplan-modal-datepicker';

	$(datepickers).datepicker({
	  daysOfWeekDisabled: [0,6],
		useCurrent: false,
	  startDate: getFirstValidDate()
	});
	$(datepickers).find('.prev').text('<');
	$(datepickers).find('.next').text('>');
	$(datepickers).datepicker('setDate', getFirstValidDate());
	$(datepickers).each(updateInput);
	$(datepickers).datepicker().on('changeDate', function () {
		var datepicker = $(this);
		datepicker.siblings('.date-hidden-input')
			.val(datepicker.datepicker('getFormattedDate'));
		$(this).closest('form').data('validator').element('.hour-input');
	});

	function updateInput() {
		var datepicker = $(this);
		datepicker.siblings('.date-hidden-input')
			.val(datepicker.datepicker('getFormattedDate'));
	}

	function getFirstValidDate() {
		var date = new Date(),
			array = [];
		if (date.getDay() == 6) {
			date = new Date(Date.now() + 2*86400000);
		} else if (date.getDay() == 0) {
			date = new Date(Date.now() + 86400000);
		}
		date.setHours(0);
		date.setMinutes(0);
		date.setSeconds(0);
		date.setMilliseconds(0);
		return date;
	}

	$('.reservation-time-button').click(function () {
			button_time = document.getElementById($(this).attr('id'));
			if (button_time.value == 'AM') {
					button_time.value = 'PM';
			} else if (button_time.value == 'PM') {
					button_time.value = 'AM';
			}
			$(this).closest('form').data('validator').element('.hour-input');
	});
})();