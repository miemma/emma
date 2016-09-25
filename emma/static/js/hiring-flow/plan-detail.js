angular.module('emmaHiringFlow')
  .controller('planDetailController', function ($scope) {
    $scope.plan = {
      allowsWorkshops: false,
      allowsActivities: false,
      workshops: [],
      activities: []
    };

    $scope.init = function (allowsWorkshops, allowsActivities) {
      $scope.plan.allowsWorkshops = allowsWorkshops;
      $scope.plan.allowsActivities = allowsActivities;
      $scope.generateLists();
    };

    $scope.generateLists = function () {
      if ($scope.plan.allowsWorkshops) {
        angular.forEach(angular.element('[data-workshop-name]'), function (elem) {
          $scope.plan.workshops.push({
            name: angular.element(elem).attr('data-workshop-name'),
            isSelected: false
          });
        });
      }
      if ($scope.plan.allowsActivities) {
        angular.forEach(angular.element('[data-activity-name]'), function (elem) {
          $scope.plan.activities.push({
            name: angular.element(elem).attr('data-activity-name'),
            isSelected: false
          });
        });
      }
    };

    $scope.showWorkshops = function () {
      console.log($scope.plan.workshops);
    };

    $scope.showActivities = function () {
      console.log($scope.plan.activities);
    };

  });