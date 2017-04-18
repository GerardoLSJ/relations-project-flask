app.controller('MainCtrl', function ($scope, $http) {
    console.log('MainCtrl')
    $scope.inputBoxes = {}
    $scope.states = []

    $scope.inputBoxes = {
        one: "1,2,3,4",
        two: "1,1",
        /*        three: "1,1",
                four: "1,1",
                five: "1,1",
                six: "1,1",
                seven: "1,1",
                eight: "1,1",
                nine: "1,1",
                ten: "1,1"*/
    }


    $scope.getResults = function () {
        var myJson = []

        angular.forEach($scope.inputBoxes, function (element) {
            if (element) {
                myJson.push(element);
            }
        });

        console.info(myJson)
        var universe = (myJson[0].split(","))
        console.log(universe)
        if (universe.length > 6) {
            return alert('Menos de 6 elementos por favor')
        }
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