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
    return function (content, singularText, pluralText) {
      content = content || 0;
      singularText = singularText || '';
      pluralText = pluralText || '';
      if (content == 1) {
        return content + ' ' + singularText;
      } else {
        return content + ' ' + pluralText;
      }
    };
  })
  .filter('pluralizeBy', function () {
    return function (singularText, dependsOn, pluralText) {
      singularText = singularText || '';
      dependsOn = dependsOn || 0;
      pluralText = pluralText || '';
      if (dependsOn == 1) {
        return singularText;
      } else {
        return pluralText;
      }
    };
  });