$(document).ready(function () {
  /* jQuery validator config
  ---------------------------------------------------------------------------*/
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

    var date = new Date();
    var actual_time = (date.getHours() *60) + date.getMinutes();
    console.log("El timepo en minutos actuales son: " + actual_time);

    var hours = parseInt($('#hourInput').val());
    var minutes = parseInt($('#timeInput').val());
    var time = $('#reservation-time-button').val();
    var total_minutes = (hours * 60) + minutes;
    if (time == 'PM') {
      total_minutes += 720;
    }
    console.log("Los minutos en la hora de la cita son: " + total_minutes);

    // Validamos que este dentro del horario de servicio
    if (total_minutes > 1200 || total_minutes < 540) {
      console.log("No esta en el horario de atención");
      return false; // No esta dentro del horario
    } else { // Si esta dentro del horario
      if ((actual_time + 45) <  total_minutes) {
        return true
      } else {
        console.log("Esta en un tiempo invalido");
        return false
      }
    }
  }, "La hora no es valida");
  
  jQuery.validator.setDefaults({
    highlight: function(element, errorClass) {
      $(element).removeClass(errorClass);
    },
    submitHandler: function (form) {
      if ($(form).find('.form-loader').length) {
        $(form).find('.form-loader').show();
      }
      if ($(form).find('.form-alert').length) {
        $(form).find('.form-alert').hide();
      }
      form.submit();
    }
  });

  /* Special forms
  ---------------------------------------------------------------------------*/
  $('.dashboard-special-form').toArray().forEach(function (elem, index) {
    var form = $(elem),
      pictures = [],
      pictureContainers = null;

    if (form.find('.form-image').length) {
      pictureContainers = form.find('.form-image');
      pictureContainers.toArray().forEach(function (elem, index) {
        pictures[index] = $(elem).css('background-image');
        $($(elem).find('input[type="file"]')).change(function (e) {
          $(elem).css('background-image', 'url("' + URL.createObjectURL(e.target.files[0]) + '")');
        });
      });
    }

    form.find('.edit-button').click(function () {
      $(this).addClass('hide');
      $(this).siblings('.cancel-button').removeClass('hide');
      $(this).siblings('.send-button').removeClass('hide');
      form.find('.input-container .fields-container')
        .removeClass('hide');
      form.find('.input-container .value-container')
        .addClass('hide');
      if (pictureContainers) {
        pictureContainers.find('label')
          .removeClass('hide');
      }
    });

    form.find('.cancel-button').click(function () {
      $(this).addClass('hide');
      $(this).siblings('.edit-button').removeClass('hide');
      $(this).siblings('.send-button').addClass('hide');
      form[0].reset();
      form.find('.input-container .fields-container')
        .addClass('hide');
      form.find('.input-container .value-container')
        .removeClass('hide');
      if (pictureContainers) {
        pictureContainers.children('label')
          .addClass('hide');
        pictureContainers.toArray().forEach(function (elem, index) {
          $(elem).css('background-image', pictures[index]);
        });
      }
    });
  });

  /* Contract Adult Form
  ---------------------------------------------------------------------------*/
  $('#contract-adult-form').validate({
    rules: {
      name: {
        required:true
      },
      last_name: {
        required:true
      },
      birthday: {
        required:true
      },
      description: {
        required:true
      },
      doctor_name: {
        required:true
      },
      doctor_phone: {
        required:true,
        number:true
      },
      doctor_cp: {
        required:true
      }
    }
  });

  /* Contract Location Form
  ---------------------------------------------------------------------------*/
  $('#contract-location-form').validate({
    rules: {
      street: {
        required:true
      },
      num_ext: {
        required:true,
        number:true
      },
      num_int: {
        required:false,
        number:true
      },
      colony: {
        required:true
      },
      delegation: {
        required:true
      },
      cp: {
        required:true,
        number:true
      },
      address_reference: {
        required:true
      },
      day_1: {
        required:true
      },
      day_1_hour: {
        required:true
      },
      start_date: {
        required:true
      },
      start_time: {
        required:true
      }
    }
  });

  /* Contract Form
  ---------------------------------------------------------------------------*/
  $('#contract-form').validate({
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
    }
	});
  
  /* Request Password Form
  ---------------------------------------------------------------------------*/
  $('#passwd-form').validate({
    rules: {
      new_password_1: {
        required: true
      },
      new_password_2: {
        required: true,
        equalTo: "#id_new_password_1"
      }
    }
  });

  /* Request Password Form
  ---------------------------------------------------------------------------*/
  $('#passwd-reset-form').validate({
    rules: {
      new_password1: {
        required: true
      },
      new_password2: {
        required: true,
        equalTo: "#id_new_password1"
      }
    }
  });

  /* Request Password Request Form
  ---------------------------------------------------------------------------*/
  $('#passwd-reset-req-form').validate({
    rules: {
      email: {
        email: true,
        required: true
      }
    }
  });

  /* Signup Form
  ---------------------------------------------------------------------------*/
  $('#signup-form').validate({
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
    }
  });
  
  /* Login Form
  ---------------------------------------------------------------------------*/
  $('#login-form').validate({
    rules: {
      username: {
        email: true
      }
    }
  });
  
  /* Date Form
  ---------------------------------------------------------------------------*/
  $('#dateForm').validate({
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
    }
  });
  
  /* Pay Form
  ---------------------------------------------------------------------------*/
  $('#pay-form').validate();
  
  /* Contact Form
  ---------------------------------------------------------------------------*/
  $('#contactForm').validate({
    errorClass: "errorWhite",
    onkeyup: false,
    onfocusout: false
  });

  /* Contact Form
  ---------------------------------------------------------------------------*/
  $('#joinForm').validate({
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
    }
  });

  /* Dashboard User Information Form
  ---------------------------------------------------------------------------*/
  $('#dashboard-user-form').validate();

  /* Dashboard Password Form
  ---------------------------------------------------------------------------*/
  $('#dashboard-password-form').validate();
});