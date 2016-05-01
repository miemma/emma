$(document).ready(function() {
  OpenPay.setId('mg0kzdwsiduimlfaudun');
  OpenPay.setApiKey('pk_106c640a77f94dd49bae11cf94937075');
  OpenPay.setSandboxMode(true);
	var deviceSessionId = OpenPay.deviceData.setup("pay-form", "devsessionid");
});
