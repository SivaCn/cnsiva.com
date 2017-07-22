
var app = angular.module("cnsiva", ['ui.router']);

app.controller("homeOnLoadCtrl", function($scope, $http, $interval) {
    /**
     * Returns a random number between min (inclusive) and max (exclusive)
     */
    function getRandomArbitrary(min, max) {
        return parseInt(Math.random() * (max - min) + min, 10);
    };

    $http
      .get("/get_quotes")
      .then(function (response) {

        $scope.allQutes = response.data;

        function update() {
          var index = getRandomArbitrary(0, $scope.allQutes.length);
          $scope.saidBy = $scope.allQutes[index][1];
          $scope.quote = $scope.allQutes[index][0];
        }
        update(); // Inital load
        $interval(update, 5000); // Interval load
    });

    $http
      .get("/get_home")
      .then(function (response) {
         $scope.page_content = response.data;
      });

}); // end: controller:homeOnLoadCtrl


app.config(function($stateProvider, $urlRouterProvider) {
  var helloState = {
    name: 'hello',
    url: '/hello',
    templateUrl: '/skills.html'
  }

  var aboutState = {
    name: 'about',
    url: '/about',
    template: '<h3>Its the UI-Router hello world app!</h3>'
  }

  $stateProvider.state(helloState);
  $stateProvider.state(aboutState);

  // Set Home Page as default
  $urlRouterProvider.when('', '/hello')

  // Route to Home Page if any wrong url is given
  $urlRouterProvider.otherwise('/hello')
});

app.controller("whoAmICtrl", function($scope, $http) {

    $http
      .get("http://localhost:3000/whoami")
      .then(function (response) {
        $scope.mainContent = response.data;
    });

}); // end: controller:whoAmICtrl

app.run(function($rootScope){

    $rootScope
        .$on('$stateChangeStart',
            function(event, toState, toParams, fromState, fromParams){
                $(".page-loading").removeClass("hidden");
        });

    $rootScope
        .$on('$stateChangeSuccess',
            function(event, toState, toParams, fromState, fromParams){
                $(".page-loading").addClass("hidden");
        });

});

