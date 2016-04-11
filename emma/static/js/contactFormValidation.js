(function () {
	var fieldsStatus = [false, false, false];

	$('#contact-name-input').change(function () {
		var validName = isValid.name(this.value);
	  paintBorderLight($(this), validName);
	  fieldsStatus[0] = validName;
	  validateForm($('#contact-submit-button'), fieldsStatus);
	});
	$('#contact-email-input').change(function () {
		var validEmail = isValid.email(this.value);
	  paintBorderLight($(this), validEmail);
	  fieldsStatus[1] = validEmail;
	  validateForm($('#contact-submit-button'), fieldsStatus);
	});
	$('#contact-message-textarea').change(function () {
		console.log(this.value);
		var validMessage = this.value != null;
	  paintBorderLight($(this), validMessage);
	  fieldsStatus[2] = validMessage;
	  validateForm($('#contact-submit-button'), fieldsStatus);
	});
})();