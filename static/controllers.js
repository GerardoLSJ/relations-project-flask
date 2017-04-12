app.controller('MainCtrl', function ($scope, $http) {
    console.log('MainCtrl')
    $scope.inputBoxes = {}


    $scope.inputBoxes = {
        one: "1,1",
        two: "2,2",
        three: "3,3",
        four: "4,4",
        five: "5,5",
        six: "6,6"
    }



    $scope.getResults = function () {
        var myJson = []
        angular.forEach($scope.inputBoxes, function (element) {
            if (element) {
                myJson.push(element);
            }
        });
        console.info(myJson)
        $http.post('/api', myJson)
            .then((res) => {
                console.info(res)
            })
            .catch((e) => {
                console.error(e)
            })
    }
})