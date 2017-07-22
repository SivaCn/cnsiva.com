
var app = angular.module("cnsiva", []);

app.controller("homeOnLoadCtrl", function($scope, $http, $interval) {
    /**
     * Returns a random number between min (inclusive) and max (exclusive)
     */
    function getRandomArbitrary(min, max) {
        return parseInt(Math.random() * (max - min) + min, 10);
    }

    $http
      .get("/get_quotes")
      .then(function (response) {

        $scope.allQutes = response.data;

        function update() {
          var index = getRandomArbitrary(0, $scope.allQutes.length);
          $scope.quote = $scope.allQutes[index][0];
          $scope.saidBy = $scope.allQutes[index][1];
        }

        update(); // Inital load

        $interval(update, 5000); // Interval load
    });

}); // end: controller:homeOnLoadCtrl

app.controller("whoAmICtrl", function($scope, $http) {

    $http
      .get("http://localhost:3000/whoami")
      .then(function (response) {
        $scope.mainContent = response.data;
    });

}); // end: controller:whoAmICtrl

