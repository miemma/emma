var isValid = (function () {
	return {
		name: function (string) {
			return /^[a-z\u00E0-\u00FC\s]+$/i.test(string);
		},
		email: function (string) {
			return /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/.test(string);
		},
		mobilePhone: function (string) {
			return /^[0-9]{10}$/.test(string);
		},
		phone: function (string) {
			return /^[0-9]{7,10}$/.test(string);
		},
		postalCode: function (string) {
			return /^[0-9]{5}$/.test(string);
		},
		age: function (string) {
			return parseInt(string) >= 30 && parseInt(string) <= 100;
		}
	};
})();

function validateForm(submitButton, fieldsStatus) {
	validFields = fieldsStatus.filter(function (element) {
	  return element == true;
	});
	submitButton.prop('disabled', validFields.length < fieldsStatus.length);
}

function paintBorder(element, isValid) {
	element.css('border', '2px ' + (isValid ? 'green':'red') + ' solid');
}

function paintBorderLight(element, isValid) {
	element.css('border', '2px ' + (isValid ? '#00ff00':'red') + ' solid');
}