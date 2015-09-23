app.factory('empresaService', function($http) {
  return {
    getEmpresas: function(callback) {
      $http.get('/directory/empresa/list/').success(callback);
    },

    putEmpresa: function(id, empresa, callback) {
        console.log(id);

      $http.put('/directory/empresa/detail/'+id,empresa).success(callback);
    }
  };
});