$('#select-plan-form button[type="submit"]').click(function (e) {
  e.preventDefault();
  var form = $('#select-plan-form')[0],
    planType = $('#select-plan-form input[name="plan"]');
  planType.val($(this).attr('data-plan'));
  form.submit();
});