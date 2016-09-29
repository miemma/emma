angular.module('emmaHiringFlow', [])
  .config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');
    })
  .filter('timeFormat', function () {
    return function (timeString) {
      timeString = timeString || '';
      var out = '',
        hours = parseInt(timeString.split(':')[0]),
        minutes = parseInt(timeString.split(':')[1]);

      if (hours > 12) {
        out = (hours - 12) + ':' + minutes;
      } else if (timeString != '') {
        out = timeString;
      } else {
        out = 'horario sin asignar'
      }

      if (hours >= 12 && hours != 24) {
        out += ' PM';
      } else if (timeString != '') {
        out += ' AM';
      }

      return out;
    };
  })
  .filter('pluralize', function () {
    return function (content, type, dependsOn, pluralLetter) {
      content = content || null;
      type = type || '';
      pluralLetter = pluralLetter || '';
      dependsOn = dependsOn || null;
      var number = typeof content == Number ? content : 0,
        singularText = '',
        pluralText = '';
      if (type == 'time') {
        singularText = 'hora';
        pluralText = 'horas';
      } else if (type == 'session') {
        singularText = 'sesión';
        pluralText = 'sesiones';
      } else if (type == '') {
        singularText = content;
        pluralText = content + pluralLetter;
      }
      if (number == 1) {
        return number + ' ' + singularText;
      } else if (pluralLetter == '') {
        return number + ' ' + pluralText;
      } else if (dependsOn == 1) {
        return singularText;
      } else {
        return pluralText;
      }
    };
  });