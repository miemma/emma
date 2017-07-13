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
    hour: {
      checkDateTime: true,
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
    basico:false,
    mixto:false,
    pro:false,
    person:false,
    appointment: false,
    customplan: false
  }
  callModalForm = null,
  callModalFormBasico = null,
  callModalFormMixto=null,
  callModalFormPro=null,
  callModalFormPerson=null,
  appointmentModalForm = null,
  customplanModalForm = null;

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

  function getSubmitHandler(modalObject, validName) {
    var submitHandler = function (form) {
      var $form = $(form).serialize(),
        sentTo = $(form).attr('action');
      validForms[validName] = true;
      $(form).find('.form-loader').show();
      $.ajax({
        url: sentTo,
        method: 'POST',
        data: $form
      })
        .done(function (data) {
          $(form).find('.form-loader').hide();
          modalObject.modal('hide');
        });
      modalObject.modal('hide');
    };
    return submitHandler;
  }

  function getOnHideFn(newModalObject, validator, formObject, validName) {
    return function () {
      var form = formObject,
        date = new Date(form.find('[name="date"]').val()),
        time = form.find('[name="hour"]').val()
          + ':' + form.find('[name="minute"]').val()
          + ' ' + form.find('[name="morning"]').val().toLowerCase(),
        year = date.getFullYear(),
        formattedDate = '';
      formattedDate = date.getDate() + ' de ' + formatMonth(date.getMonth()).toLowerCase();
      if (validForms[validName]) {
        setValues(newModalObject, {
          '.confirmation-modal__text--date': formattedDate,
          '.confirmation-modal__text--year': year,
          '.confirmation-modal__text--time': time
        });
        newModalObject.modal('toggle');
        validForms[validName] = false;
      }
      if (formObject.is('#appointment-modal__form')) {
        $('.appointment-modal__toggle').collapse('hide');
      }
      form[0].reset();
      validator.resetForm();
    };
  }


   function getOnHideFnServices(newModalObject, validator, formObject, validName) {
    return function () {
      var form = formObject;
      if (validForms[validName]) {

        newModalObject.modal('toggle');
        validForms[validName] = false;
      }
      form[0].reset();
      validator.resetForm();
    };
  }

  callModalForm = $('#call-modal__form').validate({
    groups: callGroups,
    rules: modalRules,
    submitHandler: getSubmitHandler($('#call-modal'), 'call')
  });

  callModalFormBasico = $('#call-modal__form_basico').validate({
    submitHandler: getSubmitHandler($('#call-modal_basico'), 'basico')
  });

  callModalFormMixto = $('#call-modal__form_mixto').validate({
    submitHandler: getSubmitHandler($('#call-modal_mixto'), 'mixto')
  });

  callModalFormPro = $('#call-modal__form_pro').validate({
    submitHandler: getSubmitHandler($('#call-modal_pro'), 'pro')
  });

  callModalFormPerson = $('#call-modal__form_person').validate({
    submitHandler: getSubmitHandler($('#call-modal_person'), 'person')
  });


  appointmentModalForm = $('#appointment-modal__form').validate({
    groups: appointmentGroups,
    rules: modalRules,
    submitHandler: getSubmitHandler($('#appointment-modal'), 'appointment')
  });
  customplanModalForm = $('#customplan-modal__form').validate({
    groups: customplanGroups,
    rules: modalRules,
    submitHandler: getSubmitHandler($('#customplan-modal'), 'customplan')
  });

  $('#call-modal').on('hide.bs.modal', getOnHideFn($('#call-confirmation-modal'), callModalForm, $('#call-modal__form'), 'call'));

  $('#call-modal_basico').on('hide.bs.modal', getOnHideFnServices($('#call-confirmation-modal'), callModalFormBasico, $('#call-modal__form_basico'), 'basico'));

  $('#call-modal_mixto').on('hide.bs.modal', getOnHideFnServices($('#call-confirmation-modal'), callModalFormMixto, $('#call-modal__form_mixto'), 'mixto'));

  $('#call-modal_pro').on('hide.bs.modal', getOnHideFnServices($('#call-confirmation-modal'), callModalFormPro, $('#call-modal__form_pro'), 'pro'));

  $('#call-modal_person').on('hide.bs.modal', getOnHideFnServices($('#call-confirmation-modal'), callModalFormPerson, $('#call-modal__form_person'), 'person'));


  $('#appointment-modal').on('hide.bs.modal', getOnHideFn($('#appointment-confirmation-modal'), appointmentModalForm, $('#appointment-modal__form'), 'appointment'));

  $('#customplan-modal').on('hide.bs.modal', getOnHideFn($('#customplan-confirmation-modal'), customplanModalForm, $('#customplan-modal__form'), 'customplan'));

  $('.appointment-modal__toggle-trigger').collapse('show');

  $('.appointment-modal__toggle').on('hide.bs.collapse', function () {
    $('.appointment-modal__toggle-trigger').collapse('show');
  });

  $('.appointment-modal__toggle').on('show.bs.collapse', function () {
    $('.appointment-modal__toggle-trigger').collapse('hide');
  });
})();