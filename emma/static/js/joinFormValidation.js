(function () {
	var fieldsStatus = [
		false, false, false, false, false,
		false, false, false, false, false,
		false, false, false, false, false
	];
	var checkboxes = $('[name="join-source-value"]');
	$('#join-surname-input').change(function () {
		var validSurname = isValid.name(this.value);
	  paintBorder($(this), validSurname);
	  fieldsStatus[0] = validSurname;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-name-input').change(function () {
		var validName = isValid.name(this.value);
	  paintBorder($(this), validName);
	  fieldsStatus[1] = validName;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-age-input').change(function () {
		var validAge = isValid.age(this.value);
	  paintBorder($(this), validAge);
	  fieldsStatus[2] = validAge;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-email-input').change(function () {
		var validEmail = isValid.email(this.value);
	  paintBorder($(this), validEmail);
	  fieldsStatus[3] = validEmail;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-mobilephone-input').change(function () {
		var validPhone = isValid.mobilePhone(this.value);
	  paintBorder($(this), validPhone);
	  fieldsStatus[4] = validPhone;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-phone-input').change(function () {
		var validPhone = isValid.phone(this.value);
	  paintBorder($(this), validPhone);
	  fieldsStatus[5] = validPhone;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-city-input').change(function () {
		var validCity = isValid.name(this.value);
	  paintBorder($(this), validCity);
	  fieldsStatus[7] = validCity;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-state-input').change(function () {
		var validState = isValid.name(this.value);
	  paintBorder($(this), validState);
	  fieldsStatus[8] = validState;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-delegation-input').change(function () {
		var validDelegation = isValid.name(this.value);
	  paintBorder($(this), validDelegation);
	  fieldsStatus[9] = validDelegation;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-colony-input').change(function () {
		var validColony = isValid.name(this.value);
	  paintBorder($(this), validColony);
	  fieldsStatus[10] = validColony;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('#join-postalcode-input').change(function () {
		var validCode = isValid.postalCode(this.value);
	  paintBorder($(this), validCode);
	  fieldsStatus[11] = validCode;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('[name="join-education-value"]').change(function () {
	  fieldsStatus[6] = true;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	checkboxes.change(function () {
		var selectedItems = checkboxes.filter(":checked");
		$('#join-other-input').prop('disabled', !$('#join-source-option-6').is(':checked'));
	  fieldsStatus[12] = selectedItems.length != 0;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('[name="join-facebook-value"]').change(function () {
	  fieldsStatus[13] = true;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
	$('[name="join-smartphone-value"]').change(function () {
	  fieldsStatus[14] = true;
	  validateForm($('#join-submit-button'), fieldsStatus);
	});
})();
