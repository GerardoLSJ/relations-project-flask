app.controller('MainCtrl', function ($scope, $http) {
    console.log('MainCtrl')
    $scope.states = [];
    $scope.inputBoxes = ['', ''];
    $scope.errorBoxes = [];
    $scope.inputCounter = 0;
    $scope.htmlString = '';
    $scope.universe = "1,2,3,hola"

    $scope.addPair = function () {
        $scope.inputBoxes.push('');
        console.log($scope.inputBoxes)
    };

    $scope.getResults = function () {
        var myJson = []
        myJson.push($scope.universe);
        /*
                var universe = myJson[0].split(',')
                if (universe.length > 6) {
                    return alert('Menos de 6 elementos por favor')
                }
        */
        angular.forEach($scope.inputBoxes, function (element) {
            if (element) {
                myJson.push(element);
            }
        });

        console.info(myJson)

        $http.post('/api', myJson)
            .then((res) => {
                console.info(res.data)
                $scope.states.push(res.data.data);
            })
            .catch((e) => {
                console.error(e)
            })
    }

    $scope.updatedPair = function (index) {
        //Comprueba que los elementos existen en el universo
        var universe = $scope.universe.split(',')
        var pair = $scope.inputBoxes[index].split(',')
        if (universe.indexOf(pair[0]) == -1 || universe.indexOf(pair[1]) == -1) {
            console.log("EL ELEMENTO NO EXISTE")
            $scope.errorBoxes[index] = "Alguno de los elementos no pertenece al universo";
        } else {
            $scope.errorBoxes[index] = '';
        }
        if (pair.length > 2) {
            $scope.errorBoxes[index] = "Ingresa sólo una pareja ordenada con el formato a,b"
        }
    }

    $scope.clearAll = function () {
        $scope.states = [];
        $scope.inputBoxes = ['', ''];
        $scope.errorBoxes = [];
        $scope.inputCounter = 0;
        $scope.htmlString = '';
        $scope.universe = "1,2,3,hola"
    }



})