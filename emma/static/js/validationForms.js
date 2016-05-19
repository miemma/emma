$(document).ready(function () {

  /* Contract Signup Form
  ---------------------------------------------------------------------------*/
  var $contractSignupForm = $('#contract-signup-form');
  $contractSignupForm.validate({
	    rules: {
        email: {
          email: true,
          required:true
        },
        password_1: {
          required:true
        },
        password_2: {
          required:true,
          equalTo: "#id_password_1"
        },
        name: {
          required:true
        },
        last_name: {
          required:true
        }
      },
      highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
      },
      submitHandler: function(form)  {
	      $('.contract-signup-alert').hide();
	      $('.contract-signup-loader').show();
	      form.submit();
	    }
		});

  /* Contract Form
  ---------------------------------------------------------------------------*/
  var $contractForm = $('#contract-form');
  $contractForm.validate({
	    rules: {
        "contract-service-workshop": {
          required: true,
          minlength: 1
        },
		    "contract-service": {
          required: true,
          minlength: 1
        }
	    },
	    messages: {
        "contract-service-workshop": "Selecciona al menos 1 Taller",
		    "contract-service": "Selecciona 1 Servicio"
	    },
			highlight: function(element, errorClass) {
	      $(element).removeClass(errorClass);
	    },
			submitHandler: function(form)  {
	      $('.contract-alert').hide();
	      $('.contract-loader').show();
	      form.submit();
	    }
		});
  
  /* Request Password Form
  ---------------------------------------------------------------------------*/
  var $passwdForm = $('#passwd-form');
  $passwdForm.validate({
    rules: {
      new_password_1: {
        required: true
      },
      new_password_2: {
        required: true,
        equalTo: "#id_new_password_1"
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-alert').hide();
      $('.passwd-loader').show();
      form.submit();
    }
 });

  /* Request Password Form
  ---------------------------------------------------------------------------*/
  var $passwdReset = $('#passwd-reset-form');
  $passwdReset.validate({
    rules: {
      new_password1: {
        required: true
      },
      new_password2: {
        required: true,
        equalTo: "#id_new_password1"
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-reset-alert').hide();
      $('.passwd-reset-loader').show();
      form.submit();
    }
 });

  /* Request Password Request Form
  ---------------------------------------------------------------------------*/
  var $passwdResetReq = $('#passwd-reset-req-form');
  $passwdResetReq.validate({
    rules: {
      email: {
        email: true,
        required: true
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.passwd-reset-req-alert').hide();
      $('.passwd-reset-req-loader').show();
      form.submit();
    }
 });

  /* Signup Form
  ---------------------------------------------------------------------------*/
  var $signupForm = $('#signup-form');
  $signupForm.validate({
    rules: {
      email: {
        email: true,
        required:true
      },
      password_1: {
        required:true
      },
      password_2: {
        required:true,
        equalTo: "#id_password_1"
      },
      name: {
        required:true
      },
      last_name: {
        required:true
      }
    },

    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.signup-alert').hide();
      $('.signup-loader').show();
      form.submit();
    }
  });
  
  /* Login Form
  ---------------------------------------------------------------------------*/
  var $loginForm = $('#login-form');
  $loginForm.validate({
    rules: {
      username: {
        email: true
      }
    },
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.login-alert').hide();
      $('.login-loader').show();
      form.submit();
    }
 });
  
  /* Date Form
  ---------------------------------------------------------------------------*/
  var $dateForm = $('#dateForm');
  $dateForm.validate({
    groups: {
        timeGroup: "hour minute"
    },
    rules: {
      hour: {
        number: true,
        maxlength: 12,
        minlength: 1,
        required: true
      },
      minute: {
        checkDateTime: true,
        number: true,
        maxlength: 59,
        minlength: 0,
        required: true
      },
      number: {
        number: true,
        maxlength: 10
      }
    },

    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.date-loader').show();
      form.submit();
    }
  });
  
  /* Pay Form
  ---------------------------------------------------------------------------*/
  var $payForm = $('#pay-form');
  $payForm.validate({
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.pay-loader').show();
      form.submit();
    }
  });
  
  /* Contact Form
  ---------------------------------------------------------------------------*/
  var $contactForm = $('#contactForm');
  $contactForm.validate({
    errorClass: "errorWhite",
    onkeyup: false,
    onfocusout: false,
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.emma-modal-loader').show();
      form.submit();
    }
  });

  /* Contact Form
  ---------------------------------------------------------------------------*/
  var $joinForm = $('#joinForm');
  $joinForm.validate({
    rules: {
      age: {
        number: true,
        maxlength: 2
      },
      phone_movile: {
        number: true,
        maxlength: 10
      },
      phone: {
        number: true,
        maxlength: 10
      }
    },
    highlight: function(element, errorClass) {
        $(element).removeClass(errorClass);
    },
    submitHandler: function(form)  {
      $('.join-loader').show();
      form.submit();
    }
  });

  // Mensajes de error

  jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio",
    remote: "Please fix this field.",
    email: "Ingresa una dirección de correo valida",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Ingresa un numero valido",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Los valores deben coincidir.",
    accept: "Please enter a value with a valid extension.",
    maxlength: jQuery.validator.format("No ingreses mas de {0} caracteres."),
    minlength: jQuery.validator.format("Ingresa al menos {0} caracter."),
    rangelength: jQuery.validator.format("Please enter a value between {0} and {1} characters long."),
    range: jQuery.validator.format("Inserte un valor entre {0} y {1}."),
    max: jQuery.validator.format("Inserte un valor menor o igual que {0}."),
    min: jQuery.validator.format("Inserte un valor mayor o igual que {0}.")
  });

  jQuery.validator.addMethod("checkDateTime", function(value, element) {
    var hours = parseInt($('#hourInput').val());
    var minutes = parseInt($('#timeInput').val());
    var time = $('#reservation-time-button').val();
    var total_minutes = (hours * 60) + minutes;
    console.log(total_minutes);
    if (time == 'PM') {
      total_minutes += 720;
    }
    return !(total_minutes > 1200 || total_minutes < 540);

  }, "La hora no es valida");
  
});