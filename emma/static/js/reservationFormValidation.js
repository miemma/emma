(function () {
	var fieldsStatus = [false, false, false, true, false];
	var calendarDate = $('#datepicker').datepicker('getDate');
  fieldsStatus[2] = calendarDate >= firstValidDate;
  validateForm($('#reservation-submit-button'), fieldsStatus);
	$('#my_hidden_input').val(
	  $('#datepicker').datepicker('getFormattedDate')
	);
	function setZero(element) {
 	  element.value = parseInt(element.value);
 	  if(parseInt(element.value) < 10) {
 	    element.value = '0' + element.value;
 	  }
 	}
	function validateTime() {
	  var hour = parseInt($('#reservation-hour-input').val());
	  var minute = parseInt($('#reservation-minute-input').val());
	  var am_pm = $('#reservation-time-button').text();
	  var validTime;
	  if(am_pm == 'AM') {
	  	validTime = hour >= 9 && hour <= 11;
	  }
	  else {
	    validTime = (hour >= 1 && hour <= 7) || hour == 12 || (hour == 8 && minute == 00);
	  }
    paintBorder($('#reservation-time-section'), validTime);
    paintBorder($('#reservation-time-button'), validTime);
    fieldsStatus[3] = validTime;
	  validateForm($('#reservation-submit-button'), fieldsStatus);
	};
	$('#datepicker').on("changeDate", function() {
	  $('#my_hidden_input').val(
	    $('#datepicker').datepicker('getFormattedDate')
	  );
	  calendarDate = $('#datepicker').datepicker('getDate');
	  fieldsStatus[2] = calendarDate >= firstValidDate;
	  validateForm($('#reservation-submit-button'), fieldsStatus);
	});
	$('#reservation-name-input').change(function () {
		var validName = isValid.name(this.value);
	  paintBorder($(this), validName);
	  fieldsStatus[0] = validName;
	  validateForm($('#reservation-submit-button'), fieldsStatus);
	});
	$('#reservation-email-input').change(function () {
		var validEmail = isValid.email(this.value);
	  paintBorder($(this), validEmail);
	  fieldsStatus[1] = validEmail;
	  validateForm($('#reservation-submit-button'), fieldsStatus);
	});
	$('#reservation-hour-input').change(function () {
	  if(parseInt(this.value) < 1 || this.value == '') {
	    this.value = '01';
	  }
	  if(parseInt(this.value) > 12) {
	    this.value = '12';
	  }
	  setZero(this);
	  validateTime();
	});
	$('#reservation-minute-input').change(function () {
	  if(parseInt(this.value) < 0 || this.value == '') {
	    this.value = '00';
	  }
	  if(parseInt(this.value) > 59) {
	    this.value = '59';
	  }
	  setZero(this);
	  validateTime();
	});
	$('#reservation-phone-input').change(function () {
		var validPhone = isValid.mobilePhone(this.value);
	  paintBorder($(this), validPhone);
	  fieldsStatus[4] = validPhone;
	  validateForm($('#reservation-submit-button'), fieldsStatus);
	});
})();