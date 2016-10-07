$('#select-plan-form button[type="submit"]').click(function (e) {
  e.preventDefault();
  var form = $('#select-plan-form')[0],
    planType = $('#select-plan-form input[name="plan"]');
  $(form).find('button[type="submit"]').attr('disabled', 'disabled');
  planType.val($(this).attr('data-plan'));
  $(form).siblings('.form-loader').show();
  form.submit();
});

$('#schedule-form, #emma-form').submit(function (e) {
  var form = $(this);
  form.find('.form-loader').show();
  form.find('[type="submit"]').attr('disabled', 'disabled');
});

$('[data-toggle="tooltip"]').tooltip({
  placement: 'bottom'
});