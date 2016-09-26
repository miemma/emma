angular.module('emmaHiringFlow')
  .controller('planDetailController', function ($scope, $filter) {
    $scope.plan = {
      allowsWorkshops: false,
      allowsActivities: false,
      workshops: [],
      activities: [],
      maxMonthlyHours: 0,
      maxWeeklySessions: 0,
      sessionNumbers: []
    };

    $scope.weekDays = [
      {
        text: 'Lunes',
        htmlValue: 'monday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Martes',
        htmlValue: 'tuesday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Miércoles',
        htmlValue: 'wednesday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Jueves',
        htmlValue: 'thursday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Viernes',
        htmlValue: 'friday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Sábado',
        htmlValue: 'saturday',
        isSelected: false,
        disabled: false,
        hours: 0
      },
      {
        text: 'Domingo',
        htmlValue: 'sunday',
        isSelected: false,
        disabled: false,
        hours: 0
      }
    ];

    $scope.init = function (allowsWorkshops, allowsActivities, maxMonthlyHours, maxWeeklySessions) {
      $scope.plan.allowsWorkshops = allowsWorkshops;
      $scope.plan.allowsActivities = allowsActivities;
      $scope.plan.maxMonthlyHours = maxMonthlyHours;
      $scope.plan.maxWeeklySessions = maxWeeklySessions;
      $scope.generateLists();
    };

    $scope.generateLists = function () {
      var i;
      if ($scope.plan.allowsWorkshops) {
        angular.forEach(angular.element('[data-workshop-name]'), function (elem) {
          $scope.plan.workshops.push({
            id: $scope.plan.workshops.length,
            name: angular.element(elem).attr('data-workshop-name'),
            isSelected: false
          });
        });
      }
      if ($scope.plan.allowsActivities) {
        angular.forEach(angular.element('[data-activity-name]'), function (elem) {
          $scope.plan.activities.push({
            id: $scope.plan.activities.length,
            name: angular.element(elem).attr('data-activity-name'),
            isSelected: false
          });
        });
      }
      for (i = 1; i <= $scope.plan.maxWeeklySessions; i++) {
        $scope.plan.sessionNumbers.push({
          value: i,
          text: i + (i == 1 ? ' hora' : ' horas')
        });
      }
    };

    $scope.getHoursLeft = function () {
      var selectedDays = $filter('filter')($scope.weekDays, {isSelected: true});
      var usedHours = 0;
      angular.forEach(selectedDays, function(element) {
        usedHours += element.hours;
      });
      return $scope.plan.maxMonthlyHours - usedHours;
    };

    $scope.getMergedLists = function () {
      return $scope.plan.workshops.concat($scope.plan.activities);
    };

    $scope.disableDays = function () {
      var selectedDays = $filter('filter')($scope.weekDays, {isSelected: true});
      var totalHours = 0;

      if (selectedDays.length >= $scope.plan.maxWeeklySessions) {
        $scope.weekDays = angular.forEach($scope.weekDays, function (element) {
          if (!element.isSelected) {
            element.disabled = true;
          }
        });
      } else {
        angular.forEach(selectedDays, function (element) {
          totalHours += element.hours;
        });
        if (totalHours > $scope.plan.maxMonthlyHours) {
          $scope.weekDays = angular.forEach($scope.weekDays, function (element) {
            if (!element.isSelected) {
              element.disabled = true;
            }
          });
        } else {
          $scope.weekDays = angular.forEach($scope.weekDays, function (element) {
            element.disabled = false;
          });
        }
      }
    };
  });