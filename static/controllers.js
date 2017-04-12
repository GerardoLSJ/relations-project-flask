app.controller('MainCtrl', function($scope,$http){
console.log('MainCtrl')
$scope.inputBox = "input"
var myJson = {name:"abelputo"}
$scope.getResults = function(){
    $http.post('/api', myJson)
    .then((res)=>{
        console.info(res)
    })
    .catch((e)=>{console.error(e)})
}
})