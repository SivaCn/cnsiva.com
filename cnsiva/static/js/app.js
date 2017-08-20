
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


app.controller("homePageCtrl", function($scope, $http) {

    $http
      .get("/get_home")
      .then(function (response) {

        $scope.ipAddr = response.data['ip_addr'];
        $scope.gitHub = response.data['github'];

    });

    $http
      .get("https://api.stackexchange.com/2.2/users/2820287?key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&order=desc&sort=reputation&filter=default")
      .then(function (response) {

        $scope.stackOverFlow = response.data['items'][0];

    });

}); // end: controller:homePageCtrl

app.config(function($stateProvider, $urlRouterProvider) {
  var homeState = {
    name: 'home',
    url: '/home',
    templateUrl: '/cn-home.html'
  }

  var aboutState = {
    name: 'about',
    url: '/about',
    //template: '/cn-about.html'
    templateUrl: '/cn-about.html'
  }

  var pythonBlogState = {
    name: 'pythonblog',
    url: '/pythonblog',
    templateUrl: '/cn-python-blog.html'
  }

  $stateProvider.state(homeState);
  $stateProvider.state(aboutState);
  $stateProvider.state(pythonBlogState);

  // Set Home Page as default
  $urlRouterProvider.when('', '/home')

  // Route to Home Page if any wrong url is given
  $urlRouterProvider.otherwise('/home')
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

