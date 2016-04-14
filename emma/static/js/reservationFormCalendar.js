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
	$('#datepicker').datepicker({
	  daysOfWeekDisabled: [0,6],
	  startDate: firstValidDate,
	});
	$('#datepicker .prev').text('<');
	$('#datepicker .next').text('>');

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
})();