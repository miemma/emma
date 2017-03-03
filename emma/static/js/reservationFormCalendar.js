var firstValidDate = new Date();
firstValidDate.setHours(0);
firstValidDate.setMinutes(0)
firstValidDate.setSeconds(0)
firstValidDate.setMilliseconds(0);
(function () {
	firstValidDate.setDate(firstValidDate.getDate());
	if(firstValidDate.getDay() == 0) {
	  firstValidDate.setDate(firstValidDate.getDate() + 1);
	}
	if(firstValidDate.getDay() == 6) {
	  firstValidDate.setDate(firstValidDate.getDate() + 2);
	}
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
	  startDate: firstValidDate,
	});
	$(datepickers).find('.prev').text('<');
	$(datepickers).find('.next').text('>');

	$('.reservation-time-button').click(function () {
			button_time = document.getElementById($(this).attr('id'));
			if (button_time.value == 'AM') {
					button_time.value = 'PM';
			} else if (button_time.value == 'PM') {
					button_time.value = 'AM';
			}
	});

  $(datepickers).datepicker()
	  .on('changeDate', function(e) {
			var datepicker = $(this).attr('id');
      $('.date_input[data-for="' + datepicker +  '"]').val(
          $(datepicker).datepicker('getFormattedDate')
      )
  	});
})();