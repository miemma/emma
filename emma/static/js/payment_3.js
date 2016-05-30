$(document).ready(function() {
  OpenPay.setId('mg0kzdwsiduimlfaudun');
  OpenPay.setApiKey('pk_106c640a77f94dd49bae11cf94937075');
  OpenPay.setSandboxMode(true);
	OpenPay.deviceData.setup("contract-pay-form", "devsessionid");
});

var success_callbak = function(response) {
	console.log("Bien echo");
	var token_id = response.data.id;
	$('#token_id').val(token_id);
	$('.contract-pay-alert').hide();
	$('.contract-pay-loader').show();
	$('#contract-pay-form').submit();
};

var error_callbak = function(response) {
	console.log("Error");
	$('.contract-pay-loader').hide();
	$('.contract-pay-alert').show();
};

var $contractPayForm = $('#contract-pay-form');
$contractPayForm.validate({
	onkeyup: false,
	onfocusout: false,
	groups: {
		security: "card_year card_month"
	},
	highlight: function(element, errorClass) {
			$(element).removeClass(errorClass);
	}
});

$('#contract-pay-button').on('click', function(event) {
  if ($contractPayForm.valid()) {
		$('.contract-pay-alert').hide();
		$('.contract-pay-loader').show();
		OpenPay.token.extractFormAndCreate(
			'contract-pay-form', success_callbak, error_callbak
		);
	}
});