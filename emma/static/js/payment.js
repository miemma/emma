$(document).ready(function() {
  OpenPay.setId('mg0kzdwsiduimlfaudun');
  OpenPay.setApiKey('pk_106c640a77f94dd49bae11cf94937075');
  OpenPay.setSandboxMode(true);
	OpenPay.deviceData.setup("addcard-form", "devsessionid");
});

var success_callbak = function(response) {
	var token_id = response.data.id;
	$('#token_id').val(token_id);
	$('.addcard-alert').hide();
	$('.addcard-loader').show();
	$('#addcard-form').submit();
};

var error_callbak = function(response) {
	$('.addcard-loader').hide();
	$('.addcard-alert').show();
};

var $addcardForm = $('#addcard-form');
$addcardForm.validate({
	onkeyup: false,
	onfocusout: false,
	groups: {
		security: "card_year card_month"
	},
	highlight: function(element, errorClass) {
			$(element).removeClass(errorClass);
	}
});

$('#pay-button').on('click', function(event) {
  if ($addcardForm.valid()) {
		$('.addcard-alert').hide();
		$('.addcard-loader').show();
		OpenPay.token.extractFormAndCreate(
			'addcard-form', success_callbak, error_callbak
		);
	}
});