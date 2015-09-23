app.controller('init', function($scope) {

  $scope.modelos = [{'nombre':'empresa'},];

  $scope.cargarModelo = function(modelo){
        console.log(modelo)
       $('#modelo').load('/directory/admin/'+ modelo.nombre +"/list");
   };

});


app.controller('empresasController', function($scope,empresaService) {
  $scope.empresa = '';
  $scope.empresa_id = '';

  empresaService.getEmpresas(function(results) {
   $scope.empresas = results;
  });

  $scope.habilitarEdicion = function(empresa){
      console.log('editando '+empresa.nombre + empresa.id)
      $("#editar").css("display","inline");
      $scope.empresa = empresa.nombre;
      $scope.empresa_id = empresa.id;

  };

    $scope.eliminar = function(empresa){
      console.log('eliminando '+empresa.nombre)

  };

    $scope.editar = function(){
      console.log('editando empresa ' + $scope.empresa_id + 'nuevo nombre '+ $scope.empresa);

        var nueva_empresa = {};
        nueva_empresa['nombre'] = $scope.empresa;
        //console.log(nueva_empresa);
        empresaService.putEmpresa($scope.empresa_id ,nueva_empresa ,function(results) {
                 empresaService.getEmpresas(function(results) {
                   $scope.empresas = results;
                  });
        });

  };



});