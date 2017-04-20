app.controller('MainCtrl', function ($scope, $http) {
    console.log('MainCtrl')
    $scope.states = [];
    $scope.inputBoxes = [];
    $scope.inputCounter = 0;
    $scope.htmlString = '';

    $scope.addPair = function(){
        $scope.inputBoxes.push('');
        console.log($scope.inputBoxes)
                console.log("Universe: " + $scope.universe)

    };
    $scope.getResults = function () {
        var myJson = []
        console.log("Universe: " + $scope.universe)
        myJson.push($scope.universe);

        var universe = myJson[0].split(',')
        if (universe.length > 6) {
            return alert('Menos de 6 elementos por favor')
        }
        angular.forEach($scope.inputBoxes, function (element) {
            if (element) {
                myJson.push(element);
            }
        });

        console.info(myJson)
        console.log(universe)

/*        
        for(let i = 1; i<myJson.length; i++){
            let pair = myJson[i].split(",")
            for(let j = 0; j<universe.length; j++){
              //  if(pair[0])
            }
        }
*/
        $http.post('/api', myJson)
            .then((res) => {
                console.info(res.data)
                $scope.states.push(res.data.data);
            })
            .catch((e) => {
                console.error(e)
            })
    }


})