(function () {
  var callGroups = {
    callTimeGroup: "hour minute"
  },
  appointmentGroups = {
     appointmentTimeGroup: callGroups.callTimeGroup
  },
  customplanGroups = {
    customplanTimeGroup: callGroups.callTimeGroup
  },
  modalRules = {
    // hour: {
    //   checkDateTime: true,
    //   number: true,
    //   maxlength: 12,
    //   minlength: 1,
    //   required: true
    // },
    // minute: {
    //   checkDateTime: true,
    //   number: true,
    //   maxlength: 59,
    //   minlength: 0,
    //   required: true
    // },
    phone: {
      number: true,
      maxlength: 10
    },
    description: {
      required: false
    }
  },
  validForms = {
    call: false,
    appointment: false,
    customplan: false
  }
  callModalForm,
  appointmentModalForm,
  customplanModalForm;

  function setValues(modal, data) {
    var attribute;
    for (attribute in data) {
      modal.find(attribute).html(data[attribute]);
    }
  }

  function formatMonth(month) {
    var monthName = '';
    switch (month) {
    case 1:
      monthName = 'Enero';
      break;
    case 2:
      monthName = 'Febrero';
      break;
    case 3:
      monthName = 'Marzo';
      break;
    case 4:
      monthName = 'Abril';
      break;
    case 5:
      monthName = 'Mayo';
      break;
    case 6:
      monthName = 'Junio';
      break;
    case 7:
      monthName = 'Julio';
      break;
    case 8:
      monthName = 'Agosto';
      break;
    case 9:
      monthName = 'Septiembre';
      break;
    case 10:
      monthName = 'Octubre';
      break;
    case 11:
      monthName = 'Noviembre';
      break;
    case 12:
      monthName = 'Diciembre';
      break;
    default:
      monthName = 'Desconocido';
    }
    return monthName;
  }

  callModalForm = $('#call-modal__form').validate({
    groups: callGroups,
    rules: modalRules,
    submitHandler: function (form) {
      $('#call-modal').modal('hide');
    }
  });
  appointmentModalForm = $('#appointment-modal__form').validate({
    groups: appointmentGroups,
    rules: modalRules
  });
  customplanModalForm = $('#custom-plan-modal__form').validate({
    groups: customplanGroups,
    rules: modalRules
  });

  $('#call-modal').on('hide.bs.modal', function () {
    var form = $('#call-modal__form'),
      date = new Date(form.find('[name="date"]').val()),
      time = form.find('[name="hour"]').val()
        + ':' + form.find('[name="minute"]').val()
        + ' ' + form.find('[name="morning"]').val().toLowerCase(),
      formattedDate = '';
    formattedDate = date.getDate() + ' de ' + formatMonth(date.getMonth()).toLowerCase();
    if (validForms.call) {
      setValues($('#call-confirmation-modal'), {
        '.call-confirmation-modal__text--date': formattedDate,
        '.call-confirmation-modal__text--time': time
      });
      $('#call-confirmation-modal').modal('toggle');
    }
    $('#call-modal__form')[0].reset();
    callModalForm.resetForm();
  });
})();